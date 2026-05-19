import boto3
import botocore.exceptions
import json
import sys
from datetime import datetime

sqs_client = boto3.client(
    'sqs',
    endpoint_url='http://localhost:4566',
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

QUEUE_NAME = 'qa-failures-coffee-cart'


def get_queue_url(queue_name):
    try:
        response = sqs_client.get_queue_url(QueueName=queue_name)
        return response['QueueUrl']
    except botocore.exceptions.ClientError as e:
        print(f'No se encontró la cola "{queue_name}": {e}')
        sys.exit(1)


def send_failure(suite, issues, build_id=None):
    queue_url = get_queue_url(QUEUE_NAME)

    message = {
        'suite':     suite,
        'status':    'FAIL',
        'timestamp': datetime.utcnow().isoformat(),
        'build_id':  build_id or 'local',
        'issues':    issues,
        'count':     len(issues)
    }

    try:
        response = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message),
            MessageAttributes={
                'suite': {
                    'StringValue': suite,
                    'DataType':    'String'
                },
                'severity': {
                    'StringValue': 'HIGH' if len(issues) > 3 else 'MEDIUM',
                    'DataType':    'String'
                }
            }
        )
        print(f'Fallo enviado a SQS — suite: {suite} | MessageId: {response["MessageId"]}')
        return response['MessageId']
    except botocore.exceptions.ClientError as e:
        print(f'Error enviando mensaje a SQS: {e}')
        raise


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print('Uso: python send_failure.py <suite> "<issue1>" "<issue2>" ...')
        print('Ejemplo: python send_failure.py newman "3 assertions fallidas" "timeout superado"')
        sys.exit(1)

    suite  = sys.argv[1]
    issues = sys.argv[2:]
    send_failure(suite, issues)