
# QA Repository — Coffee Cart

Proyecto de automatización QA para https://coffee-cart.app.
Incluye pruebas de API, end-to-end, performance, seguridad,
accesibilidad y testing de infraestructura cloud, integradas
en un pipeline Jenkins con Docker.

---

## Herramientas

| Tipo          | Herramienta         | Descripción                              |
|---------------|---------------------|------------------------------------------|
| API           | Postman / Newman    | Pruebas de endpoints REST                |
| E2E           | Cypress             | Pruebas de interfaz y flujos de usuario  |
| Performance   | JMeter / BlazeMeter | Carga con 20, 50, 80 y 100 usuarios      |
| Seguridad     | OWASP ZAP           | Análisis de vulnerabilidades             |
| Accesibilidad | Axe / Lighthouse    | Cumplimiento WCAG                        |
| Cloud         | LocalStack / boto3  | Simulación de servicios AWS              |
| CI/CD         | Jenkins             | Pipeline automatizado                    |
| Contenedores  | Docker / Compose    | Aislamiento de cada suite                |

---

## Estructura del proyecto
qa-repository-coffee-cart/
├── api-testing/            Pruebas de API con Postman y Newman
│   ├── postman/            Colecciones y entornos
│   ├── newman/             Runner CLI y reportes
│   └── results-docker/     Resultados generados en pipeline
├── automation/             Pruebas E2E con Cypress
│   ├── cypress/            Tests, fixtures y configuración
│   └── Dockerfile          Imagen para correr Cypress en pipeline
├── performance/            Pruebas de carga
│   ├── jmeter/             Planes de prueba y resultados
│   └── blazemeter/         Evidencia de ejecución en nube
├── security/               Análisis de seguridad
│   └── zap-analysis/       Reportes OWASP ZAP
├── accesibility-testing/   Pruebas de accesibilidad
│   ├── axe/                Código de análisis
│   └── lighthouse/         Reportes HTML
├── cloud-testing/          Infraestructura AWS con LocalStack
│   ├── aws/                Scripts Python por servicio
│   └── localstack/         Docker Compose de LocalStack
├── bug-reports/            Reportes de bugs con evidencia y Jira
├── test-scenarios/         Escenarios de prueba documentados
├── results-docker/         Resultados consolidados del pipeline
├── results-jenkins/        Capturas y resumen del pipeline
├── docker-compose.yml      Orquestación principal del pipeline
├── Jenkinsfile             Definición del pipeline CI/CD
└── set-up.sh               Verificación del entorno local

---

## Arquitectura del pipeline
Jenkins
|
+-- docker-compose.yml
|
+-- [api-test]     Newman en Docker  → results-docker/newman/
+-- [cypress-test] Cypress en Docker → results-docker/cypress/
+-- [jmeter]       JMeter en Docker  → results-docker/jmeter/
+-- [zap]          OWASP ZAP         → results-docker/zap/
|
+-- LocalStack (AWS simulado)
|
+-- S3        Almacena reportes por suite y fecha
+-- SQS       Cola de notificaciones de fallos
+-- DynamoDB  Historial de ejecuciones
+-- Lambda    Validación automática de resultados

Cada suite corre en su propio contenedor Docker definido en `docker-compose.yml`.
Los resultados se centralizan en `results-docker/` y luego se suben a S3.

---

## Requisitos

- Docker Engine
- Docker Compose
- Python 3.12 (para cloud-testing)
- Jenkins con acceso a Docker socket

---

## Setup inicial

Verificar el entorno antes de correr el pipeline:

```bash
bash set-up.sh
```

El script verifica que Docker esté instalado, que el daemon esté activo
y que `docker-compose.yml` esté presente.

Para la parte de cloud testing, el pipeline Jenkins instala las dependencias
Python automáticamente en cada ejecución. Para correr cloud testing localmente:

```bash
cd cloud-testing
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd localstack && docker compose up -d
bash ../aws/scripts/setup_all.sh
```

---

## Correr el pipeline

El pipeline se ejecuta desde Jenkins apuntando al repositorio.
En cada build Jenkins:

1. Levanta LocalStack
2. Inicializa servicios AWS (S3, SQS, DynamoDB, Lambda)
3. Corre Newman (API)
4. Corre Cypress (E2E)
5. Corre JMeter (performance)
6. Corre OWASP ZAP (seguridad)
7. Sube todos los reportes a S3
8. Registra metadata en DynamoDB
9. Revisa la cola SQS para determinar si el build pasa o falla
10. Apaga todos los contenedores

---

## Correr suites individualmente

```bash
# API - Newman
cd api-testing && bash run-docker.sh

# E2E - Cypress
cd automation && bash run.sh

# Performance - JMeter
cd performance/jmeter && bash run.sh

# Seguridad - ZAP
docker compose up zap
```

---

## Resultados

Los reportes se generan en `results-docker/` durante el pipeline y se
archivan en Jenkins. Adicionalmente, se suben a S3 en LocalStack
organizados por suite y fecha de ejecución.

---

## Documentación por módulo

Cada directorio principal tiene su propio README con instrucciones
específicas de setup y ejecución.
