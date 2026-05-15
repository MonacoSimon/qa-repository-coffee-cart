# API Testing - Coffee Cart

Este módulo contiene pruebas automatizadas de API realizadas con Postman y Newman sobre la aplicación Coffee Cart.

Las pruebas validan comportamiento funcional, disponibilidad de endpoints, contenido de respuestas y tiempos de respuesta.

La ejecución puede realizarse:

- localmente con Newman
- mediante Docker
- integrada en pipelines CI/CD

---

# Estructura del proyecto

```text
api-testing/
├── newman/
│   ├── inform.md
│   ├── newman.sh
│   ├── README.sh
│   └── results-newman/
│       └── report.html
│
├── postman/
│   ├── collections/
│   │   └── api-testing-coffee-cart.postman_collection.json
│   │
│   ├── enviroment/
│   │   └── environment-coffee-cart.postman_environment.json
│   │
│   └── results/
│
├── results-docker/
│   └── report.json
│
└── run-docker.sh
```

---

# Objetivo

Validar endpoints y comportamiento HTTP de la aplicación Coffee Cart mediante pruebas automatizadas.

Las validaciones incluyen:

- códigos de estado HTTP
- contenido HTML esperado
- tiempos de respuesta
- respuestas no vacías
- disponibilidad de rutas
- comportamiento de parámetros especiales

---

# Herramientas utilizadas

- Postman
- Newman
- Docker
- JSON Reports

---

# Colección utilizada

La colección principal se encuentra en:

```text
postman/collections/api-testing-coffee-cart.postman_collection.json
```

El entorno utilizado:

```text
postman/enviroment/environment-coffee-cart.postman_environment.json
```

---

# Endpoints probados

## GET /

Página principal de Coffee Cart.

Validaciones:

- respuesta HTML válida
- contenido esperado
- tiempo de respuesta aceptable

---

## GET /cart

Página del carrito.

Validaciones:

- respuesta HTML válida
- carga correcta de la vista
- contenido esperado

---

## GET /github

Redirección o acceso al repositorio del proyecto.

Validaciones:

- disponibilidad del endpoint
- respuesta válida

---

## GET /?breakable=1

Simulación de errores internos de la aplicación.

Validaciones:

- disponibilidad del sitio
- respuesta válida aún en modo breakable

---

## GET /?ad=1

Carga de publicidad y contenido adicional.

Validaciones:

- respuesta válida
- contenido HTML correcto
- estabilidad del sitio con ads habilitados

---

# Ejecución local con Newman

## Instalar Newman

```bash
npm install -g newman
```

---

## Ejecutar colección

```bash
newman run postman/collections/api-testing-coffee-cart.postman_collection.json \
-e postman/enviroment/environment-coffee-cart.postman_environment.json \
--env-var "urlBase=https://coffee-cart.app/"
```

---

# Ejecución mediante Docker

El proyecto incluye ejecución containerizada utilizando la imagen oficial de Newman.

## Dar permisos al script

```bash
chmod +x run-docker.sh
```

---

## Ejecutar pruebas

```bash
./run-docker.sh
```

---

# Reportes

Los resultados generados mediante Docker se almacenan en:

```text
results-docker/report.json
```

Los reportes locales de Newman se almacenan en:

```text
newman/results-newman/
```

---

# Resultados obtenidos

## Resumen de ejecución

| Métrica | Resultado |
|---|---|
| Requests ejecutadas | 5 |
| Assertions | 25 |
| Fallos | 0 |
| Tiempo promedio | 85 ms |
| Tiempo mínimo | 48 ms |
| Tiempo máximo | 225 ms |
| Duración total | 607 ms |

---

# Observaciones QA

Las pruebas muestran:

- alta estabilidad funcional
- respuestas rápidas
- ausencia de errores HTTP
- correcta disponibilidad de endpoints

La aplicación mantiene tiempos de respuesta bajos incluso utilizando parámetros especiales como:

```text
?ad=1
?breakable=1
```

---

# Integración CI/CD

Este módulo está preparado para integrarse en pipelines automatizados como Jenkins.

Flujo típico:

1. Ejecutar colección Postman
2. Generar reportes JSON
3. Analizar resultados
4. Publicar artefactos
5. Integrar métricas QA

---

# Posibles mejoras

- agregar validaciones JSON Schema
- incorporar pruebas POST/PUT/DELETE
- generar reportes HTML avanzados
- integrar métricas en AWS CloudWatch
- automatizar análisis de resultados
- ejecutar pruebas paralelas

---

# Enfoque QA

Este módulo prioriza:

- automatización reproducible
- portabilidad mediante Docker
- desacoplamiento entre tests y entorno
- integración sencilla en CI/CD
- validación rápida de endpoints web

```
