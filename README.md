# QA Repository — Coffee Cart

Proyecto de automatización QA integral para https://coffee-cart.app. Incluye pruebas de API, End-to-End (E2E), rendimiento, seguridad, accesibilidad y testing de infraestructura Cloud, orquestadas dinámicamente mediante un pipeline de Jenkins sobre contenedores Docker.

---

## Herramientas y Tecnologías

| Capa de Testing | Herramienta | Descripción Técnica |
|---|---|---|
| API Testing | Postman / Newman | Validación de endpoints REST y automatización CLI |
| E2E Automation | Cypress | Pruebas de interfaz bajo arquitectura Page Object Model (POM) |
| Performance | JMeter / BlazeMeter | Pruebas de carga e inyección con 20, 50, 80 y 100 usuarios hilos |
| Security Testing | OWASP ZAP | Escaneo dinámico (DAST) y análisis de vulnerabilidades |
| Accesibilidad | Axe / Lighthouse | Auditoría automatizada bajo estándares WCAG |
| Cloud Testing | LocalStack / Boto3 | Emulación local de servicios AWS (S3, SQS, DynamoDB, Lambda) |
| Orquestación CI/CD | Jenkins | Pipeline declarativo estructurado en etapas |
| Contenedores | Docker / Compose | Aislamiento y portabilidad de entornos de ejecución |

---

## Estructura del Proyecto

```text
qa-repository-coffee-cart/
├── accesibility-testing/      # Pruebas de accesibilidad (Axe y Lighthouse)
│   ├── axe/                   # Scripts de integración y análisis
│   ├── lighthouse/            # Reportes HTML de rendimiento y UX
│   └── inform.md              # Informe consolidado de accesibilidad
├── api-testing/               # Pruebas de API automatizadas
│   ├── postman/               # Colecciones y entornos de variables
│   ├── newman/                # Automatización de ejecución CLI
│   ├── results-docker/        # Resultados de API generados en contenedor
│   └── run-docker.sh          # Script de ejecución local para Newman
├── automation/                # Pruebas E2E con Cypress (Arquitectura POM)
│   ├── cypress/               # Tests, selectores, páginas y configuración
│   ├── Dockerfile             # Definición de imagen aislada para Cypress
│   └── run.sh                 # Script de inicialización de la suite
├── bug-reports/               # Reportes formales de fallas encontradas
│   ├── bug-report.ods         # Matriz detallada de defectos (ODS)
│   ├── bug-report.pdf         # Matriz detallada de defectos (PDF)
│   ├── evidence/              # Capturas y logs de fallas
│   └── jira/                  # Mapeo y tickets asociados a Jira
├── cloud-testing/             # Infraestructura AWS emulada
│   ├── aws/                   # Scripts de automatización en Python (Boto3)
│   ├── localstack/            # Configuración y aprovisionamiento local
│   └── requirements.txt       # Dependencias de Python para el entorno Cloud
├── conclusions/               # Resumen final del proyecto de calidad
│   └── inform.md              # Informe ejecutivo de QA
├── performance/               # Pruebas de rendimiento y estrés
│   ├── jmeter/                # Scripts JMX y reportes de latencia
│   └── blazemeter/            # Reportes en nube distribuidos
├── results-docker/            # Centralización local de reportes generados
│   ├── jmeter/                # Logs e informes de rendimiento
│   ├── newman/                # Reportes JSON/HTML de APIs
│   └── zap/                   # Reportes de vulnerabilidades
├── results-jenkins/           # Evidencias de ejecución en servidor CI/CD
│   ├── pipeline-inform.md     # Estado y tiempos de las etapas
│   └── screenshots/           # Capturas de pantallas del proceso
├── security/                  # Análisis de vulnerabilidades web
│   ├── zap-analysis/          # Sesiones y mapeos de ataque
│   └── inform.md              # Informe de seguridad estático
├── test-scenarios/            # Diseño e ingeniería de pruebas
│   ├── test-scenarios.ods     # Matrices de casos de prueba (ODS)
│   └── test-scenarios.pdf     # Matrices de casos de prueba (PDF)
├── docker-compose.yml         # Orquestación de servicios y suites
├── Jenkinsfile                # Pipeline declarativo de integración continua
├── requirements.txt           # Dependencias de Python del proyecto raíz
└── set-up.sh                  # Script de validación de entorno local

Arquitectura del Pipeline

El flujo de integración continua administra el ciclo de vida completo de las pruebas, abstrayendo las dependencias del sistema operativo mediante contenedores independientes.
Plaintext

Jenkins
 │
 ├── docker-compose.yml (Orquestación de infraestructura y runners)
 │
 ├── [api-test]      Newman en Docker  --> results-docker/newman/
 ├── [cypress-test]  Cypress en Docker --> results-docker/cypress/ (Patrón POM)
 ├── [jmeter]        JMeter en Docker  --> results-docker/jmeter/
 ├── [zap]           OWASP ZAP DAST    --> results-docker/zap/
 │
 └── LocalStack (Entorno Cloud AWS Aislado)
      ├── Amazon S3        --> Almacenamiento perenne de reportes por fecha
      ├── Amazon SQS       --> Cola de mensajería para manejo de fallas
      ├── Amazon DynamoDB  --> Historial analítico de ejecuciones de la suite
      └── AWS Lambda       --> Validación serverless automática de resultados

Cada suite de pruebas se ejecuta de forma aislada dentro de su propio contenedor definido en docker-compose.yml. Los resultados son extraídos de los contenedores hacia el directorio results-docker/ y posteriormente cargados en el bucket de S3 emulado.
Requisitos del Sistema

    Docker Engine (Versión reciente instalada y activa)

    Docker Compose

    Python 3.12 (Solo requerido para desarrollo o ejecución local de scripts Cloud)

    Servidor Jenkins configurado con acceso al socket de Docker (/var/run/docker.sock)

Configuración Inicial (Setup)

Antes de realizar la ejecución del pipeline o de suites individuales, valide el estado del entorno local corriendo:
Bash

bash set-up.sh

Este script automatizado confirma la presencia de las herramientas críticas de Docker y la estructura del proyecto.
Configuración Manual del Módulo Cloud

El pipeline automatiza este proceso. Si requiere depurar o ejecutar las pruebas de infraestructura de AWS de manera local, ejecute:
Bash

cd cloud-testing
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cd localstack && docker compose up -d
bash ../aws/scripts/setup_all.sh

Ejecución del Pipeline Completo

El ciclo de automatización está diseñado para ser gatillado de manera remota desde Jenkins apuntando a este repositorio. Al ejecutarse, el archivo Jenkinsfile realiza los siguientes pasos de manera secuencial:

    Limpieza de espacios de trabajo previos.

    Inicialización de LocalStack y aprovisionamiento de recursos AWS (S3, SQS, DynamoDB, Lambda).

    Ejecución de pruebas de endpoints mediante Newman.

    Ejecución de automatización de interfaz con Cypress usando Page Object Model (POM).

    Inyección de cargas de rendimiento controladas con Apache JMeter.

    Escaneo dinámico de vulnerabilidades de seguridad a través de OWASP ZAP.

    Extracción y empaquetamiento de reportes hacia Amazon S3 ordenados por marcas de tiempo.

    Persistencia de metadatos de la corrida actual en tablas de DynamoDB.

    Consumo y procesamiento de colas SQS para la determinación automatizada del estado del build (Pass/Fail).

    Desmantelamiento de contenedores y limpieza del entorno de ejecución (Teardown).

Ejecución de Suites Individuales

Si requiere aislar ejecuciones y realizar pruebas granulares en su entorno local, puede invocar los siguientes comandos:
Bash

# Suite de API (Postman / Newman)
cd api-testing && bash run-docker.sh

# Suite E2E (Cypress con arquitectura POM)
cd automation && bash run.sh

# Suite de Rendimiento (Apache JMeter)
cd performance/jmeter && bash run.sh

# Suite de Seguridad (OWASP ZAP)
docker compose up zap

Resultados y Reportabilidad

Los reportes y evidencias en crudo se unifican transitoriamente en el directorio local results-docker/ durante el transcurso del pipeline. Al finalizar el proceso, la persistencia se realiza en LocalStack, alojando los archivos en Amazon S3 bajo esquemas de nombres normalizados basados en la fecha y el componente evaluado. Los reportes consolidados definitivos e históricos de Jenkins se encuentran accesibles dentro de los módulos results-jenkins/ y conclusions/.