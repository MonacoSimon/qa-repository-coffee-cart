#!/bin/bash
set -e

LOCALSTACK_URL="${LOCALSTACK_URL:-http://localhost:4566}"
FUNCTION_NAME="qa-validate-results"
DIR="$(cd "$(dirname "$0")" && pwd)"
VENV_PYTHON="$(dirname "$(dirname "$(dirname "$DIR")")")/venv/bin/python"
ZIP_FILE="$DIR/function.zip"

echo "========================================"
echo "  Deploy Lambda: $FUNCTION_NAME"
echo "========================================"

echo "Empaquetando handler..."
cd "$DIR"
zip -j "$ZIP_FILE" handler.py
echo "function.zip generado"

echo "Deployando con Python/boto3..."
"$VENV_PYTHON" - <<EOF
import boto3, base64, os

client = boto3.client(
    'lambda',
    endpoint_url='$LOCALSTACK_URL',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

with open('$ZIP_FILE', 'rb') as f:
    zip_bytes = f.read()

try:
    client.get_function(FunctionName='$FUNCTION_NAME')
    client.update_function_code(FunctionName='$FUNCTION_NAME', ZipFile=zip_bytes)
    print('Lambda actualizada')
except client.exceptions.ResourceNotFoundException:
    client.create_function(
        FunctionName='$FUNCTION_NAME',
        Runtime='python3.12',
        Role='arn:aws:iam::000000000000:role/lambda-role',
        Handler='handler.lambda_handler',
        Code={'ZipFile': zip_bytes}
    )
    print('Lambda creada')

print('========================================')
print(f'  Deploy finalizado: $FUNCTION_NAME')
print('========================================')
EOF

rm -f "$ZIP_FILE"