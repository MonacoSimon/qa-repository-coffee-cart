#!/bin/bash
set -e

LOCALSTACK_URL="http://host.docker.internal:4566"
CLOUD_DIR="$(cd "$(dirname "$0")/.." && pwd)"

echo "========================================"
echo "  QA Cloud Setup — coffee-cart"
echo "========================================"

echo ""
echo "Verificando LocalStack..."
MAX_RETRIES=10
RETRY=0
until curl -s "$LOCALSTACK_URL/_localstack/health" | grep -q '"s3": "available"' 2>/dev/null; do
    RETRY=$((RETRY + 1))
    if [ $RETRY -ge $MAX_RETRIES ]; then
        echo "LocalStack no responde después de $MAX_RETRIES intentos."
        echo "   Ejecutá: docker compose up -d (en cloud-testing/localstack/)"
        exit 1
    fi
    echo "   Esperando LocalStack... intento $RETRY/$MAX_RETRIES"
    sleep 3
done
echo "LocalStack disponible"


if [ ! -d "$CLOUD_DIR/../venv/bin" ]; then
    echo "Creando virtualenv..."
    python3 -m venv "$CLOUD_DIR/../venv"
fi

source "$CLOUD_DIR/../venv/bin/activate"
echo "Virtualenv activado"

echo "Instalando dependencias Python..."
pip install --quiet boto3 botocore

echo ""
echo "[1/4] Configurando S3..."
python "$CLOUD_DIR/s3/setup_bucket.py"

echo ""
echo "[2/4] Configurando SQS..."
python "$CLOUD_DIR/sqs/setup_queue.py"

echo ""
echo "[3/4] Configurando DynamoDB..."
python "$CLOUD_DIR/dynamodb/setup_table.py"

echo ""
echo "[4/4] Deployando Lambda..."
bash "$CLOUD_DIR/lambda/validate_results/deploy.sh"

echo ""
echo "========================================"
echo "Setup completo"
echo ""
echo "  Servicios disponibles en $LOCALSTACK_URL:"
echo "    S3        → qa-reports-coffee-cart"
echo "    S3        → qa-s3-auto-bucket"
echo "    SQS       → qa-failures-coffee-cart"
echo "    DynamoDB  → qa_executions"
echo "    Lambda    → qa-validate-results"
echo "========================================"