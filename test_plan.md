# Test Plan — QA Repository Coffee Cart

## Por qué existe este documento

Este repo ya tiene bastante testing andando: API, E2E, performance, seguridad, accesibilidad y hasta una simulación de infraestructura cloud. Lo que faltaba era un lugar donde explicar el *por qué* de todo eso — qué estamos cubriendo, qué no, y qué significa que un build "pase" o "falle". Eso es lo que intenta resolver este Test Plan.

No es un documento para llenar un casillero. La idea es que cualquiera que entre al repo —yo en seis meses, otro QA, un reclutador evaluando el proyecto— entienda la estrategia completa sin tener que leer el Jenkinsfile línea por línea.

---

## 1. Alcance

### Qué se prueba

La aplicación bajo prueba es [Coffee Cart](https://coffee-cart.app), una app de e-commerce simple (carrito de compras de café) que sirve como target ideal para practicar todo el espectro de testing sin la complejidad de un sistema real en producción.

Se cubren estas dimensiones:

| Dimensión | Qué valida | Herramienta |
|---|---|---|
| API | Contratos de los endpoints REST, respuestas esperadas, casos negativos | Postman / Newman |
| End-to-end | Flujos de usuario reales en el navegador (agregar al carrito, pagar, etc.) | Cypress |
| Manual / exploratorio | Casos puntuales y exploración libre que la automatización no cubre (todavía) o que conviene verificar a ojo antes de automatizar | Ejecución manual, documentado en `test-scenarios/` |
| Performance | Comportamiento bajo carga (20, 50, 80 y 100 usuarios concurrentes) | JMeter / BlazeMeter |
| Seguridad | Vulnerabilidades conocidas (OWASP Top 10 básico) | OWASP ZAP |
| Accesibilidad | Cumplimiento WCAG mínimo | Axe / Lighthouse |
| Infraestructura | Simulación de servicios AWS que soportan el pipeline (no la app en sí) | LocalStack / boto3 |

### Qué NO se prueba (por ahora)

Para ser honesto sobre el alcance:

- **Testing visual/cross-browser exhaustivo**: Cypress corre en un solo browser configurado, no hay matriz de compatibilidad.
- **Pruebas de penetración profundas**: ZAP corre en modo automático (baseline scan), no hay pentesting manual ni explotación de vulnerabilidades encontradas.
- **Performance a gran escala**: 100 usuarios concurrentes es un techo razonable para un proyecto de práctica, no representa carga de producción real.
- **Mobile testing**: no hay suite específica para viewports móviles ni apps nativas.

Esto no es una limitación oculta — es una decisión consciente de alcance para mantener el proyecto manejable y enfocado.

---

## 2. Estrategia por tipo de prueba

### API (Postman/Newman)
Se valida que los endpoints devuelvan los códigos de estado, estructura y datos esperados, incluyendo casos donde se espera que la API falle controladamente (inputs inválidos, recursos inexistentes). Las colecciones corren vía Newman dentro de un contenedor Docker para que el resultado sea siempre el mismo, sin importar quién o desde dónde se ejecute.

### End-to-end (Cypress)
Se simulan los flujos que un usuario real haría: entrar al sitio, agregar productos al carrito, modificar cantidades, completar el checkout. La idea es detectar regresiones visuales o funcionales que las pruebas de API no pueden ver, porque ahí no hay UI de por medio.

### Manual / exploratorio
No todo se automatiza de entrada. Antes de escribir un test de Cypress, suelo recorrer el flujo a mano para entender bien el comportamiento esperado y detectar casos raros que no se me hubieran ocurrido mirando solo el código. Esos casos quedan registrados como escenarios en `test-scenarios/`, y si algo falla, el hallazgo se documenta en `bug-reports/` con evidencia (capturas, pasos de reproducción) como si fuera un ticket real. Es la parte más "humana" del proceso: cosas como ver si un mensaje de error confunde, si una animación tapa un botón, o si el flujo se siente raro aunque técnicamente "funcione" — ahí la automatización todavía no llega tan bien como el ojo de alguien probando.

### Performance (JMeter/BlazeMeter)
Se ejecutan pruebas de carga incremental (20 → 100 usuarios) para identificar en qué punto el tiempo de respuesta empieza a degradarse. No buscamos romper el sistema, buscamos entender su curva de comportamiento.

### Seguridad (OWASP ZAP)
Un escaneo automático contra la aplicación para detectar vulnerabilidades comunes (headers de seguridad ausentes, exposición de información, problemas de configuración). Es una primera línea de defensa, no un análisis exhaustivo.

### Accesibilidad (Axe/Lighthouse)
Se valida que la aplicación cumpla con criterios básicos de WCAG — contraste, etiquetas ARIA, navegación por teclado — para asegurar que no se está dejando afuera a usuarios con alguna discapacidad.

### Infraestructura cloud (LocalStack)
Esto es un poco distinto al resto: no es testing *de* la aplicación, es testing *de la infraestructura que soporta el testing*. Se simulan S3, SQS, DynamoDB y Lambda localmente para validar que el pipeline pueda guardar resultados, encolar notificaciones de fallos y registrar historial sin depender de una cuenta de AWS real.

---

## 3. Ambientes

| Ambiente | Para qué se usa |
|---|---|
| Local (Docker Compose) | Desarrollo y debug de cada suite individualmente |
| CI (Jenkins) | Ejecución completa del pipeline en cada build |
| Cloud simulado (LocalStack) | Persistencia de resultados sin costos ni credenciales reales de AWS |

La razón de tener todo dockerizado es simple: que el test corra igual en mi máquina que en el servidor de Jenkins. Si algo falla, falla por el código o el ambiente de la app, no porque "en mi compu funcionaba".

---

## 4. Criterios de entrada y salida

**Para empezar a correr el pipeline (entrada):**
- El código de la aplicación bajo prueba está accesible (coffee-cart.app responde).
- Docker y Docker Compose están disponibles en el entorno (se valida con `set-up.sh`).
- Las dependencias de Python para cloud-testing están instaladas si se corre esa suite.

**Para considerar un build exitoso (salida):**
- Todas las pruebas de API pasan sin fallos críticos.
- Los flujos E2E principales (agregar al carrito, checkout) completan sin errores.
- No aparecen vulnerabilidades de severidad alta o crítica en el escaneo de ZAP.
- Los tiempos de respuesta bajo carga no superan los umbrales definidos en los planes de JMeter.
- No hay regresiones de accesibilidad respecto al baseline anterior.

**Sobre los fallos — no todos pesan igual:**
Un fallo de seguridad o de E2E debería bloquear el pipeline. Un fallo de accesibilidad o una alerta de performance, si es menor, puede registrarse como advertencia sin frenar todo — la idea es no transformar el pipeline en un cuello de botella por cosas que no son bloqueantes pero sí merecen seguimiento. Esta distinción hoy se gestiona manualmente revisando los reportes; es una mejora pendiente automatizarla en el Jenkinsfile.

---

## 5. Riesgos conocidos

Sin vueltas, estos son los puntos débiles actuales del proyecto:

- **Dependencia de un sitio externo**: coffee-cart.app es un proyecto de terceros pensado para práctica. Si cambia su estructura o deja de estar disponible, varias suites (E2E, API, performance) se ven afectadas sin que sea un problema de este repo.
- **Cobertura de seguridad limitada**: un baseline scan de ZAP da una foto general, pero no reemplaza un análisis de seguridad serio. No hay que confundir "pasó ZAP" con "es seguro".
- **Sin alertas automáticas de degradación de performance**: hoy se mira el reporte de JMeter manualmente después de cada corrida; no hay un umbral que falle el build automáticamente si el tiempo de respuesta empeora.
- **Single point of failure en Jenkins**: todo el pipeline depende de una sola instancia de Jenkins. No hay redundancia ni hay documentado un plan de recuperación si esa instancia cae.

Documentar esto no es para "quedar mal" — es justamente la diferencia entre un proyecto que sabe sus propios límites y uno que los esconde.

---

## 6. Roles y responsabilidades

Este es un proyecto personal, así que hoy todos los roles caen en una sola persona. Aun así, vale la pena separarlos conceptualmente porque es como se estructuraría en un equipo real:

| Rol | Responsabilidad |
|---|---|
| QA Engineer | Diseño y mantenimiento de las suites de prueba, análisis de resultados |
| DevOps / CI | Mantenimiento del pipeline de Jenkins y la orquestación con Docker |
| Responsable de reportes | Triage de bugs encontrados, documentación en `bug-reports/` |

---

## 7. Métricas que importan

No todas las métricas dicen lo mismo, así que estas son las que se siguen de cerca:

- **Tasa de éxito del pipeline**: porcentaje de builds que pasan todas las suites sin intervención manual.
- **Tiempo total del pipeline**: cuánto tarda desde que arranca Jenkins hasta que sube los resultados a S3 (simulado). Si crece mucho, hay que revisar si alguna suite se volvió lenta innecesariamente.
- **Cantidad y severidad de hallazgos de ZAP**: no solo cuántos, sino qué tan graves.
- **Cobertura de escenarios E2E**: cuántos de los flujos críticos de usuario están efectivamente cubiertos por Cypress vs. los que quedan solo documentados en `test-scenarios/`.
- **Bugs encontrados manualmente vs. en automatización**: si la mayoría de los hallazgos vienen siempre del testing manual, es una señal de que la automatización todavía no está mirando donde debería.

---

## 8. Relación con el resto del repo

Para que quede claro cómo se conecta todo:

- **`test-scenarios/`** contiene los casos de prueba documentados a mano — tanto los que después se automatizan en Cypress/Newman como los que se quedan en exploración manual porque no vale la pena (o todavía no) automatizarlos. Este Test Plan es el "por qué", esa carpeta es el "qué exactamente se probó".
- **`bug-reports/`** documenta los hallazgos de esos casos manuales (y de cualquier suite automatizada), con evidencia y seguimiento tipo Jira. Si una prueba manual encuentra un bug, ahí queda el rastro completo: qué se hizo, qué se esperaba, qué pasó en realidad.
- **`results-docker/` y `results-jenkins/`** son la evidencia de que el plan efectivamente se ejecuta, no solo se documenta.

---
