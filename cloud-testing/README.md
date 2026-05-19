# Cloud Testing — QA Coffee Cart

Este módulo implementa infraestructura AWS simulada con LocalStack para
demostrar integración de servicios cloud dentro de un pipeline de QA.
La aplicación bajo prueba (https://coffee-cart.app) corre en producción;
los servicios AWS se usan como infraestructura de soporte para el pipeline,
no para hostear la app.

---

## Concepto

En proyectos reales, QA usa servicios cloud para almacenar resultados,
validar umbrales automáticamente y registrar historial de ejecuciones.
Este módulo replica ese flujo usando LocalStack como emulador local de AWS.
Pipeline Jenkins
|
+-- [Cypress]  → reporte HTML → S3 → DynamoDB registra
+-- [Newman]   → reporte JSON → S3 → DynamoDB registra
+-- [JMeter]   → reporte JTL  → S3 → DynamoDB registra
+-- [ZAP]      → reporte HTML → S3 → DynamoDB registra
|
+-- Lambda valida resultados
+-- SQS recibe mensajes de fallo
+-- poll_failures.py determina si Jenkins falla el build

---

## Estructura
cloud-testing/
├── aws/
│   ├── s3/
│   │   ├── setup_bucket.py       Crea los buckets necesarios en LocalStack
│   │   └── upload_reports.py     Sube los reportes de cada suite al bucket
│   ├── sqs/
│   │   ├── setup_queue.py        Crea la cola principal y la Dead Letter Queue
│   │   ├── send_failure.py       Publica un mensaje de fallo en la cola
│   │   └── poll_failures.py      Lee la cola y determina si el build falla
│   ├── dynamodb/
│   │   ├── setup_table.py        Crea la tabla qa_executions
│   │   └── record_execution.py   Guarda metadata de cada ejecución
│   ├── lambda/
│   │   └── validate_results/
│   │       ├── handler.py        Lógica de validación por suite (Newman, JMeter, Cypress, ZAP)
│   │       └── deploy.sh         Empaqueta y despliega la función en LocalStack
│   └── scripts/
│       ├── setup_all.sh          Inicializa todos los servicios en orden
│       └── teardown_all.sh       Elimina todos los recursos creados
├── localstack/
│   └── docker-compose.yml        Define el contenedor LocalStack con S3, SQS, DynamoDB, Lambda
├── reports/                      Directorio para reportes locales
├── requirements.txt              Dependencias Python del módulo
└── venv/                         Entorno virtual (no versionado)

---

## Servicios AWS simulados

### S3 — Almacenamiento de reportes

Bucket principal: `qa-reports-coffee-cart`

Los reportes se organizan por suite y fecha:
qa-reports-coffee-cart/
cypress/2026-05-19/report.html
newman/2026-05-19/report.json
jmeter/2026-05-19/Test-Plan-100-users.jtl
zap/2026-05-19/report.html

Bucket de prueba: `qa-s3-auto-bucket`, usado por `setup_bucket.py` para
verificar que el ciclo completo de creación, subida y descarga funciona.

### SQS — Cola de notificaciones de fallos

Cola principal: `qa-failures-coffee-cart`
Dead Letter Queue: `qa-failures-dlq-coffee-cart` (reintentos: 3)

Cuando una suite falla, `send_failure.py` publica un mensaje con el detalle.
Al final del pipeline, `poll_failures.py` lee la cola y termina con exit code 1
si hay mensajes, lo que hace que Jenkins marque el build como fallido.

### DynamoDB — Historial de ejecuciones

Tabla: `qa_executions`
Partition key: `suite` (String)
Sort key: `timestamp` (String)

Cada ejecución registra: suite, estado (PASS/FAIL), duración, total de tests,
tests fallidos, porcentaje de aprobación y build ID de Jenkins.

### Lambda — Validación de resultados

Función: `qa-validate-results`

Recibe el payload de resultados de cada suite y valida contra umbrales:

| Suite   | Validación                                      |
|---------|-------------------------------------------------|
| Newman  | 0 assertions fallidas, tiempo promedio < 2000ms |
| JMeter  | tasa de error < 5%, tiempo promedio < 2000ms    |
| Cypress | 0 tests fallidos                                |
| ZAP     | 0 alertas HIGH, menos de 5 alertas MEDIUM       |

Retorna `PASS` con HTTP 200 o `FAIL` con HTTP 422.

---

## Flujo completo

setup_all.sh     → levanta S3, SQS, DynamoDB, Lambda en LocalStack
Suites de prueba → Cypress, Newman, JMeter, ZAP generan reportes
upload_reports.py → sube todos los reportes a S3 por suite y fecha
record_execution.py → guarda metadata de cada ejecución en DynamoDB
poll_failures.py → revisa SQS; si hay mensajes de fallo, el build falla


---

## Requisitos

- Docker y Docker Compose
- Python 3.12+

---

## Setup local

```bash
cd cloud-testing
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Levantar LocalStack:

```bash
cd localstack
docker compose up -d
```

Verificar que esté disponible:

```bash
curl http://localhost:4566/_localstack/health
```

Inicializar todos los servicios AWS:

```bash
bash aws/scripts/setup_all.sh
```

---

## Correr scripts individualmente

```bash
# S3
python aws/s3/setup_bucket.py
python aws/s3/upload_reports.py

# SQS
python aws/sqs/setup_queue.py
python aws/sqs/poll_failures.py

# DynamoDB
python aws/dynamodb/setup_table.py
python aws/dynamodb/record_execution.py cypress PASS 45 12 0 local

# Lambda
bash aws/lambda/validate_results/deploy.sh
```

---

## Teardown

```bash
bash aws/scripts/teardown_all.sh
cd localstack && docker compose down
```

---

## Integración con Jenkins

El pipeline levanta LocalStack, corre el setup, ejecuta las suites y
en el bloque `post { always }` sube reportes, registra en DynamoDB
y revisa la cola SQS. LocalStack se apaga al final del pipeline.

Ver `Jenkinsfile` en la raíz del proyecto para el detalle completo.
