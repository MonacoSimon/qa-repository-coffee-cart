import boto3
import botocore.exceptions
import json

sqs_client = boto3.client(
    'sqs',
    endpoint_url="${LOCALSTACK_URL:-http://localhost:4566}",
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

QUEUE_NAME     = 'qa-failures-coffee-cart'
DLQ_NAME       = 'qa-failures-dlq-coffee-cart'  


def create_queue(queue_name, attributes=None):
    try:
        response = sqs_client.create_queue(
            QueueName=queue_name,
            Attributes=attributes or {}
        )
        url = response['QueueUrl']
        print(f'Cola creada: "{queue_name}"')
        print(f'   URL: {url}')
        return url
    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'QueueAlreadyExists':
            response = sqs_client.get_queue_url(QueueName=queue_name)
            url = response['QueueUrl']
            print(f'ℹCola ya existe: "{queue_name}" → {url}')
            return url
        print(f'Error creando cola "{queue_name}": {e}')
        raise


def get_queue_arn(queue_url):
    response = sqs_client.get_queue_attributes(
        QueueUrl=queue_url,
        AttributeNames=['QueueArn']
    )
    return response['Attributes']['QueueArn']


if __name__ == "__main__":
    print("=" * 50)
    print("  SQS Setup — qa-failures")
    print("=" * 50)

    dlq_url = create_queue(DLQ_NAME)
    dlq_arn = get_queue_arn(dlq_url)
    print(f'   ARN DLQ: {dlq_arn}')
    print()

    redrive_policy = json.dumps({
        'deadLetterTargetArn': dlq_arn,
        'maxReceiveCount': '3'  
    })

    main_url = create_queue(QUEUE_NAME, attributes={
        'VisibilityTimeout':      '30',
        'MessageRetentionPeriod': '86400',  
        'RedrivePolicy':          redrive_policy
    })

    print()
    print("=" * 50)
    print(f'  Cola principal : {QUEUE_NAME}')
    print(f'  Dead Letter    : {DLQ_NAME}')
    print("=" * 50)