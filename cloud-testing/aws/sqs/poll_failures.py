import boto3
import botocore.exceptions
import json
import sys
import os

sqs_client = boto3.client(
    'sqs',
    endpoint_url=os.environ.get('LOCALSTACK_URL', 'http://localhost:4566'),
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

QUEUE_NAME   = 'qa-failures-coffee-cart'
MAX_MESSAGES = 10


def get_queue_url(queue_name):
    try:
        response = sqs_client.get_queue_url(QueueName=queue_name)
        return response['QueueUrl']
    except botocore.exceptions.ClientError as e:
        print(f' No se encontró la cola "{queue_name}": {e}')
        sys.exit(1)


def poll_and_report():
    queue_url = get_queue_url(QUEUE_NAME)
    all_failures = []

    print("=" * 55)
    print("  SQS Poll — Revisando fallos del pipeline")
    print("=" * 55)

    while True:
        response = sqs_client.receive_message(
            QueueUrl=queue_url,
            MaxNumberOfMessages=MAX_MESSAGES,
            MessageAttributeNames=['All'],
            WaitTimeSeconds=2          
        )

        messages = response.get('Messages', [])
        if not messages:
            break

        for msg in messages:
            body = json.loads(msg['Body'])
            all_failures.append(body)

            suite     = body.get('suite', '?')
            count     = body.get('count', 0)
            timestamp = body.get('timestamp', '')
            issues    = body.get('issues', [])

            print(f' FALLO — Suite: {suite.upper()} | {timestamp}')
            print(f'   Issues ({count}):')
            for issue in issues:
                print(f'     • {issue}')

            sqs_client.delete_message(
                QueueUrl=queue_url,
                ReceiptHandle=msg['ReceiptHandle']
            )

    print("\n" + "=" * 55)

    if not all_failures:
        print('Sin fallos en la cola — pipeline OK')
        print("=" * 55)
        sys.exit(0)
    else:
        suites_fallidas = list({f['suite'] for f in all_failures})
        print(f'{len(all_failures)} suite(s) con fallos: {", ".join(suites_fallidas)}')
        print("=" * 55)
        sys.exit(1) 

if __name__ == "__main__":
    poll_and_report()