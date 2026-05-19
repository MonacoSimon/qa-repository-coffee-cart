#!/bin/bash

LOCALSTACK_URL="http://localhost:4566"
CLOUD_DIR="$(cd "$(dirname "$0")/.." && pwd)"
AWS_CMD="aws --endpoint-url=$LOCALSTACK_URL --region us-east-1"

echo "========================================"
echo "  QA Cloud Teardown — coffee-cart"
echo "========================================"
echo "[1/4] Eliminando S3..."
for bucket in "qa-reports-coffee-cart" "qa-s3-auto-bucket"; do
    if $AWS_CMD s3api head-bucket --bucket "$bucket" 2>/dev/null; then
        $AWS_CMD s3 rm "s3://$bucket" --recursive --quiet
        $AWS_CMD s3api delete-bucket --bucket "$bucket"
        echo "Bucket eliminado: $bucket"
    else
        echo "Bucket no existe: $bucket"
    fi
done

echo "[2/4] Eliminando SQS..."
for queue in "qa-failures-coffee-cart" "qa-failures-dlq-coffee-cart"; do
    URL=$($AWS_CMD sqs get-queue-url --queue-name "$queue" --query 'QueueUrl' --output text 2>/dev/null || echo "")
    if [ -n "$URL" ]; then
        $AWS_CMD sqs delete-queue --queue-url "$URL"
        echo "Cola eliminada: $queue"
    else
        echo "Cola no existe: $queue"
    fi
done

echo "[3/4] Eliminando DynamoDB..."
if $AWS_CMD dynamodb describe-table --table-name qa_executions &>/dev/null; then
    $AWS_CMD dynamodb delete-table --table-name qa_executions
    echo "Tabla eliminada: qa_executions"
else
    echo "Tabla no existe: qa_executions"
fi

echo "[4/4] Eliminando Lambda..."
if $AWS_CMD lambda get-function --function-name qa-validate-results &>/dev/null; then
    $AWS_CMD lambda delete-function --function-name qa-validate-results
    echo "Lambda eliminada: qa-validate-results"
else
    echo "Lambda no existe: qa-validate-results"
fi

echo ""
echo "  ✅ Teardown completo"