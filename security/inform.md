# Security – Análisis de seguridad con OWASP ZAP

# Descripción

Este módulo contiene el análisis de seguridad de la aplicación web Coffee Cart utilizando OWASP ZAP ejecutado dentro de un entorno Dockerizado.

El objetivo del análisis es detectar:

* configuraciones inseguras
* exposición de información
* debilidades en cabeceras HTTP
* posibles vectores de ataque
* malas prácticas de seguridad web

El análisis fue realizado mediante un escaneo automatizado baseline (pasivo).

---

# Herramienta utilizada

* OWASP ZAP (Zed Attack Proxy)
* Ejecución mediante Docker
* Imagen utilizada:

```bash
zaproxy/zap-stable
```

---

# Ejecución del análisis

El análisis se ejecutó mediante:

```bash
./run.sh
```

Internamente:

```bash
docker run -t -u root \
-v $(pwd):/zap/wrk \
zaproxy/zap-stable \
zap-baseline.py \
-t https://coffee-cart.app \
-r report.html
```

---

# Tipo de análisis realizado

El escaneo baseline de ZAP:

* realiza análisis pasivo
* inspecciona respuestas HTTP
* detecta configuraciones inseguras
* no ejecuta ataques activos
* no modifica datos de la aplicación

---

# Resumen de hallazgos

* Vulnerabilidades críticas: 0
* Vulnerabilidades medias: 5 tipos
* Vulnerabilidades bajas: 5 tipos
* Hallazgos informativos: múltiples
* Total de alertas: 25

---

# Distribución de alertas

| Tipo de alerta | Riesgo | Cantidad |
|---|---|---|
| CSP Header Not Set | Medio | 5 |
| Falta atributo Subresource Integrity | Medio | 5 |
| Falta cabecera Anti-Clickjacking | Medio | 5 |
| Session ID en URL | Medio | 3 |
| Configuración Incorrecta Cross-Domain (CORS) | Medio | 2 |
| Falta encabezado X-Content-Type-Options | Bajo | 6 |
| Strict-Transport-Security no configurado | Bajo | 7 |
| Inclusión JS entre dominios | Bajo | 5 |
| Timestamp Disclosure | Bajo | 5 |
| Divulgación de versión servidor | Bajo | 3 |

---

# Vulnerabilidades detectadas

## Cabecera Content Security Policy (CSP) no configurada

**Riesgo:** Medio

### Descripción

La aplicación no define una política CSP en las respuestas HTTP.

### Impacto

Esto incrementa el riesgo de:

* Cross-Site Scripting (XSS)
* carga de scripts maliciosos
* ejecución de contenido no confiable

### Recomendación

Agregar cabecera:

```http
Content-Security-Policy: default-src 'self';
```

---

## Falta atributo de integridad de recursos secundarios (SRI)

**Riesgo:** Medio

### Descripción

Los recursos externos cargados desde CDN no utilizan hashes de integridad.

### Impacto

Si el recurso remoto es comprometido, el navegador ejecutará código alterado sin validación.

### Recomendación

Implementar atributos:

```html
integrity=""
crossorigin="anonymous"
```

---

## Falta cabecera Anti-Clickjacking

**Riesgo:** Medio

### Descripción

La aplicación no implementa protección contra clickjacking.

### Impacto

La aplicación podría ser embebida dentro de iframes maliciosos.

### Recomendación

Agregar:

```http
X-Frame-Options: DENY
```

o:

```http
Content-Security-Policy: frame-ancestors 'none';
```

---

## Configuración Incorrecta Cross-Domain (CORS)

**Riesgo:** Medio

### Descripción

Se detectaron políticas CORS permisivas sobre recursos externos.

### Impacto

Puede permitir interacción indebida desde dominios externos.

### Recomendación

Restringir orígenes permitidos:

```http
Access-Control-Allow-Origin: https://dominio-seguro.com
```

---

## Session ID en URL

**Riesgo:** Medio

### Descripción

Se detectaron identificadores de sesión enviados en parámetros URL.

### Impacto

Los IDs pueden quedar expuestos en:

* logs
* historial del navegador
* proxies
* herramientas de monitoreo

### Recomendación

Utilizar cookies seguras y evitar tokens en URLs.

---

# Vulnerabilidades de bajo riesgo

## Falta encabezado X-Content-Type-Options

### Impacto

El navegador puede interpretar incorrectamente tipos MIME.

### Recomendación

Agregar:

```http
X-Content-Type-Options: nosniff
```

---

## Strict-Transport-Security no configurado

### Impacto

Los navegadores podrían permitir conexiones inseguras HTTP.

### Recomendación

Agregar:

```http
Strict-Transport-Security: max-age=31536000; includeSubDomains
```

---

## Inclusión de JavaScript entre dominios

### Impacto

Dependencia de scripts externos incrementa la superficie de ataque.

### Recomendación

Minimizar dependencias externas y validar integridad.

---

## Divulgación de timestamps Unix

### Impacto

Puede exponer información temporal interna del servidor.

### Recomendación

Evitar timestamps innecesarios en respuestas públicas.

---

## Divulgación de versión del servidor

### Impacto

Facilita fingerprinting y reconocimiento tecnológico.

### Recomendación

Ocultar cabeceras:

```http
Server
X-Powered-By
```

---

# Hallazgos informativos

Durante el análisis se detectó:

* aplicación SPA (Single Page Application)
* frontend desarrollado con Vue.js
* uso de Google Analytics
* uso de Google Tag Manager
* despliegue sobre Netlify
* uso de recursos CDN externos
* uso de HTTP/3
* múltiples recursos cacheados

---

# Tecnologías detectadas

| Tecnología | Detectada |
|---|---|
| Vue.js | Sí |
| Netlify | Sí |
| Google Analytics | Sí |
| Google Tag Manager | Sí |
| Cloudflare CDN | Sí |
| HTTP/3 | Sí |

---

# Análisis general

La aplicación presenta una postura de seguridad relativamente estable para un entorno de 
demostración/testing.

No se detectaron:

* vulnerabilidades críticas
* ejecución remota de código
* exposición directa de credenciales
* fallos severos de autenticación

Sin embargo, sí se observan múltiples debilidades relacionadas con:

* cabeceras HTTP faltantes
* políticas de seguridad incompletas
* dependencia de recursos externos
* exposición de metadatos

---

# Recomendaciones generales

## Hardening HTTP

Implementar:

* CSP
* HSTS
* X-Frame-Options
* X-Content-Type-Options

---

## Seguridad frontend

* utilizar Subresource Integrity
* reducir scripts externos
* validar dependencias CDN

---

## Seguridad de sesión

* evitar tokens en URLs
* usar cookies HttpOnly y Secure

---

## Exposición de información

* ocultar versiones del servidor
* reducir comentarios y metadatos
* limitar información pública innecesaria

---

# Conclusión

El análisis automatizado con OWASP ZAP no detectó vulnerabilidades críticas en Coffee Cart.

La aplicación presenta una arquitectura moderna y estable, pero mantiene varias debilidades 
comunes relacionadas con configuración de seguridad web.

Los principales puntos a mejorar son:

* cabeceras HTTP de protección
* control de políticas CSP
* protección anti-clickjacking
* reducción de exposición de información
* validación de recursos externos

En su estado actual, la aplicación resulta adecuada para entornos de testing y aprendizaje 
QA, aunque requeriría tareas de hardening antes de utilizarse en un entorno productivo 
real.
