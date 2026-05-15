# Informe de pruebas con Newman (API Testing)

## Descripción

Este módulo contiene pruebas automatizadas de API ejecutadas con Newman (CLI de Postman) 
sobre la aplicación web [Coffee Cart](https://coffee-cart.app/?utm_source=chatgpt.com).

El objetivo de las pruebas fue validar:

- disponibilidad de endpoints
- estabilidad de respuestas HTTP
- tiempos de respuesta
- contenido esperado del frontend
- funcionamiento de rutas accesibles públicamente

Las pruebas se ejecutaron mediante colecciones de Postman automatizadas con Newman.

---

# Resumen de ejecución

```text
┌─────────────────────────┬───────────────────┬───────────────────┐
│                         │          executed │            failed │
├─────────────────────────┼───────────────────┼───────────────────┤
│              iterations │                 1 │                 0 │
├─────────────────────────┼───────────────────┼───────────────────┤
│                requests │                 5 │                 0 │
├─────────────────────────┼───────────────────┼───────────────────┤
│            test-scripts │                 5 │                 0 │
├─────────────────────────┼───────────────────┼───────────────────┤
│      prerequest-scripts │                 0 │                 0 │
├─────────────────────────┼───────────────────┼───────────────────┤
│              assertions │                25 │                 0 │
├─────────────────────────┴───────────────────┴───────────────────┤
│ total run duration: 537ms                                       │
├─────────────────────────────────────────────────────────────────┤
│ total data received: 4.69kB (approx)                            │
├─────────────────────────────────────────────────────────────────┤
│ average response time: 76ms [min: 47ms, max: 190ms, s.d.: 56ms] │
└─────────────────────────────────────────────────────────────────┘
```

---

# Métricas generales

| Métrica | Resultado |
|---|---|
| Total Assertions | 25 |
| Total Failed Tests | 0 |
| Total Skipped Tests | 0 |
| Requests ejecutadas | 5 |
| Tiempo promedio de respuesta | 76 ms |
| Tiempo mínimo | 47 ms |
| Tiempo máximo | 190 ms |
| Datos recibidos | 4.69 kB |
| Duración total | 537 ms |

---

# Configuración del entorno

| Parámetro | Valor |
|---|---|
| Herramienta | Postman + Newman |
| Tipo de pruebas | API Testing |
| Ejecución | Local mediante CLI |
| Colección | api-testing-coffee-cart |
| Base URL | https://coffee-cart.app/ |

---

# Casos de prueba ejecutados

## GET requests

### Get index

```http
GET /
```

Status: `200 OK`

Validaciones realizadas:

- respuesta HTML válida
- contenido esperado presente
- existencia del formulario principal
- tiempo de respuesta aceptable
- respuesta no vacía

---

### Cart

```http
GET /cart
```

Status: `200 OK`

Validaciones realizadas:

- respuesta HTML válida
- contenido esperado presente
- carga correcta de la vista del carrito
- tiempo de respuesta aceptable
- respuesta no vacía

---

### Github

```http
GET /github
```

Status: `200 OK`

Validaciones realizadas:

- respuesta HTML válida
- navegación correcta hacia recurso externo
- contenido esperado presente
- tiempo de respuesta aceptable
- respuesta no vacía

---

### Breakable cart

```http
GET /?breakable=1
```

Status: `200 OK`

Validaciones realizadas:

- respuesta HTML válida
- simulación correcta del modo breakable
- contenido esperado presente
- tiempo de respuesta aceptable
- respuesta no vacía

---

### App with ads

```http
GET /?ad=1
```

Status: `200 OK`

Validaciones realizadas:

- respuesta HTML válida
- carga correcta de contenido con publicidad simulada
- contenido esperado presente
- tiempo de respuesta aceptable
- respuesta no vacía

---

# Resultados obtenidos

## Estabilidad

Las pruebas finalizaron exitosamente sin errores funcionales.

Se observa:

- 100 % de requests exitosas
- 0 fallos de ejecución
- 0 assertions fallidas
- respuestas consistentes en todos los endpoints evaluados

---

## Rendimiento

El tiempo promedio de respuesta fue de 76 ms, considerado bajo para una aplicación web pública.

Distribución observada:

- mínimo: 47 ms
- máximo: 190 ms
- desviación estándar: 56 ms

Esto indica:

- respuestas rápidas
- baja latencia
- comportamiento estable bajo ejecución simple

---

## Validaciones funcionales

Las pruebas permitieron verificar correctamente:

- accesibilidad de endpoints públicos
- disponibilidad de páginas principales
- correcta entrega de contenido HTML
- presencia de elementos esperados en la interfaz
- estabilidad básica del frontend

---

# Observaciones QA

La aplicación Coffee Cart presenta una arquitectura orientada principalmente a frontend 
testing y automatización E2E.

Durante las pruebas se observó que:

- gran parte de la lógica funciona del lado cliente
- no existe una API REST pública compleja
- las rutas responden principalmente contenido HTML
- algunas funcionalidades utilizan tracking externo (Google Analytics)

Por este motivo, la aplicación resulta especialmente útil para:

- Cypress
- Selenium
- Playwright
- pruebas E2E
- accessibility testing
- performance testing
- security scanning
- pruebas visuales

más que para pruebas avanzadas de APIs REST autenticadas.

---

# Conclusiones

Las pruebas ejecutadas con Newman muestran que la aplicación responde de forma estable y 
consistente.

Se destaca:

- 100 % de éxito en requests y assertions
- tiempos de respuesta bajos
- correcta disponibilidad de endpoints públicos
- estabilidad general del frontend

La aplicación resulta adecuada para:

- automatización QA
- validaciones funcionales básicas
- integración CI/CD
- pruebas automatizadas con Postman/Newman

En escenarios de testing API más avanzados, se recomienda complementar este proyecto con 
aplicaciones específicamente diseñadas para APIs REST, como:

- Restful Booker
- ReqRes
- JSONPlaceholder
- Swagger Petstore
