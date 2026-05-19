import boto3
import botocore.exceptions
import json
import sys
from datetime import datetime

dynamodb = boto3.client(
    'dynamodb',
    endpoint_url="http://localhost:4566",
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

TABLE_NAME = 'qa_executions'


def record(suite, status, duration_s=0, total_tests=0, failed_tests=0, build_id='local', notes=''):
    timestamp = datetime.utcnow().isoformat()
    item = {
        'suite':        {'S': suite},
        'timestamp':    {'S': timestamp},
        'status':       {'S': status},            
        'build_id':     {'S': str(build_id)},
        'duration_s':   {'N': str(duration_s)},
        'total_tests':  {'N': str(total_tests)},
        'failed_tests': {'N': str(failed_tests)},
        'pass_rate':    {'S': f'{((total_tests - failed_tests) / total_tests * 100):.1f}%' if total_tests else 'N/A'},
        'notes':        {'S': notes}
    }

    try:
        dynamodb.put_item(TableName=TABLE_NAME, Item=item)
        print(f'Registrado en DynamoDB: {suite} | {status} | {timestamp}')
    except botocore.exceptions.ClientError as e:
        print(f' Error guardando en DynamoDB: {e}')
        raise


def query_suite_history(suite, limit=10):
    try:
        response = dynamodb.query(
            TableName=TABLE_NAME,
            KeyConditionExpression='suite = :s',
            ExpressionAttributeValues={':s': {'S': suite}},
            ScanIndexForward=False,     # más reciente primero
            Limit=limit
        )

        items = response.get('Items', [])
        print(f'Historial de "{suite}" (últimas {len(items)} ejecuciones):')
        print(f'  {"Timestamp":<25} {"Status":<6} {"Tests":<7} {"Fallos":<7} {"Pass%":<8} Build')
        print(f'  {"-"*65}')
        for item in items:
            print(
                f'  {item["timestamp"]["S"]:<25}'
                f'{item["status"]["S"]:<6}'
                f'{item["total_tests"]["N"]:<7}'
                f'{item["failed_tests"]["N"]:<7}'
                f'{item["pass_rate"]["S"]:<8}'
                f'{item["build_id"]["S"]}'
            )
        return items
    except botocore.exceptions.ClientError as e:
        print(f'Error consultando historial: {e}')
        raise


def scan_all_latest():
    try:
        response = dynamodb.scan(TableName=TABLE_NAME)
        items = response.get('Items', [])
        print(f'Todas las ejecuciones registradas ({len(items)} total):')
        for item in sorted(items, key=lambda x: x['timestamp']['S'], reverse=True):
            status_icon = 'paso' if item['status']['S'] == 'PASS' else 'fallo'
            print(f'  {status_icon} [{item["suite"]["S"]:>8}] {item["timestamp"]["S"]} — {item["status"]["S"]}')
    except botocore.exceptions.ClientError as e:
        print(f'Error en scan: {e}')

if __name__ == "__main__":
    if len(sys.argv) >= 3:
        suite        = sys.argv[1]
        status       = sys.argv[2]
        duration_s   = int(sys.argv[3])   if len(sys.argv) > 3 else 0
        total_tests  = int(sys.argv[4])   if len(sys.argv) > 4 else 0
        failed_tests = int(sys.argv[5])   if len(sys.argv) > 5 else 0
        build_id     = sys.argv[6]        if len(sys.argv) > 6 else 'local'

        record(suite, status, duration_s, total_tests, failed_tests, build_id)
        query_suite_history(suite)
    else:
        print("Modo demo — insertando datos de ejemplo...")
        record('cypress', 'PASS', 45,  12, 0, 'build-001')
        record('newman',  'PASS', 12,   8, 0, 'build-001')
        record('jmeter',  'FAIL', 120, 50, 3, 'build-001', 'timeout en /checkout')
        record('zap',     'PASS', 90,   0, 0, 'build-001')
        scan_all_latest()