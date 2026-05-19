#!/bin/bash
set -e

LOCALSTACK_URL="http://localhost:4566"
FUNCTION_NAME="qa-validate-results"
HANDLER="handler.lambda_handler"
RUNTIME="python3.12"
ROLE="arn:aws:iam::000000000000:role/lambda-role"
ZIP_FILE="function.zip"
DIR="$(cd "$(dirname "$0")" && pwd)"

echo "========================================"
echo "  Deploy Lambda: $FUNCTION_NAME"
echo "========================================"

echo "Empaquetando handler..."
cd "$DIR"
zip -j "$ZIP_FILE" handler.py
echo "$ZIP_FILE generado"

EXISTING=$(aws lambda get-function \
  --function-name "$FUNCTION_NAME" \
  --endpoint-url "$LOCALSTACK_URL" \
  --region us-east-1 \
  --output text 2>/dev/null || echo "NOT_FOUND")

if echo "$EXISTING" | grep -q "NOT_FOUND"; then
  echo "Creando función Lambda..."
  aws lambda create-function \
    --function-name "$FUNCTION_NAME" \
    --runtime "$RUNTIME" \
    --role "$ROLE" \
    --handler "$HANDLER" \
    --zip-file "fileb://$ZIP_FILE" \
    --endpoint-url "$LOCALSTACK_URL" \
    --region us-east-1
  echo "Lambda creada"
else
  echo "Actualizando función Lambda existente..."
  aws lambda update-function-code \
    --function-name "$FUNCTION_NAME" \
    --zip-file "fileb://$ZIP_FILE" \
    --endpoint-url "$LOCALSTACK_URL" \
    --region us-east-1
  echo "Lambda actualizada"
fi

echo ""
echo "Smoke test..."
RESPONSE=$(aws lambda invoke \
  --function-name "$FUNCTION_NAME" \
  --payload '{"suite":"newman","results":{"run":{"stats":{"assertions":{"failed":0}},"failures":[],"timings":{"responseAverage":300}}}}' \
  --endpoint-url "$LOCALSTACK_URL" \
  --region us-east-1 \
  /tmp/lambda-smoke-response.json \
  --output text)

cat /tmp/lambda-smoke-response.json
echo ""
echo "Smoke test completado"

rm -f "$ZIP_FILE"
echo "========================================"
echo "  Deploy finalizado: $FUNCTION_NAME"
echo "========================================"