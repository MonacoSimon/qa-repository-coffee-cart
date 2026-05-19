import boto3
import botocore.exceptions

dynamodb = boto3.client(
    'dynamodb',
    endpoint_url="${LOCALSTACK_URL:-http://localhost:4566}",
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

TABLE_NAME = 'qa_executions'


def create_table():
    try:
        dynamodb.create_table(
            TableName=TABLE_NAME,
            KeySchema=[
                {'AttributeName': 'suite',     'KeyType': 'HASH'},   # partition key
                {'AttributeName': 'timestamp', 'KeyType': 'RANGE'}   # sort key
            ],
            AttributeDefinitions=[
                {'AttributeName': 'suite',     'AttributeType': 'S'},
                {'AttributeName': 'timestamp', 'AttributeType': 'S'}
            ],
            BillingMode='PAY_PER_REQUEST'
        )
        print(f'Tabla "{TABLE_NAME}" creada exitosamente.')

    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'ResourceInUseException':
            print(f'ℹTabla "{TABLE_NAME}" ya existe.')
        else:
            print(f'Error creando tabla: {e}')
            raise


def verify_table():
    try:
        response = dynamodb.describe_table(TableName=TABLE_NAME)
        status = response['Table']['TableStatus']
        print(f'   Estado: {status}')
        return status == 'ACTIVE'
    except botocore.exceptions.ClientError as e:
        print(f' No se pudo verificar la tabla: {e}')
        return False


if __name__ == "__main__":
    print("=" * 50)
    print("  DynamoDB Setup — qa_executions")
    print("=" * 50)
    create_table()
    verify_table()
    print("=" * 50)