import boto3
import botocore.exceptions
import os
from datetime import datetime

s3_client = boto3.client(
    's3',
    endpoint_url=os.environ.get('LOCALSTACK_URL', 'http://localhost:4566'),
    aws_access_key_id='test',
    aws_secret_access_key='test',
    region_name='us-east-1'
)

BUCKET_NAME = 'qa-reports-coffee-cart'
DATE_PREFIX = datetime.now().strftime('%Y-%m-%d')

REPORTS = {
    'cypress': 'automation/cypress/results',          
    'newman': 'results-docker/newman',
    'jmeter': 'results-docker/jmeter',
    'zap': 'results-docker/zap',
}

VALID_EXTENSIONS = {
    'cypress': ['.html', '.json', '.xml'],
    'newman':  ['.json', '.html'],
    'jmeter':  ['.jtl', '.html', '.csv'],
    'zap':     ['.html', '.xml', '.json'],
}


def ensure_bucket_exists(bucket_name):
    try:
        s3_client.head_bucket(Bucket=bucket_name)
        print(f'Bucket "{bucket_name}" ya existe.')
    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '404':
            s3_client.create_bucket(Bucket=bucket_name)
            print(f'Bucket "{bucket_name}" creado exitosamente.')
        else:
            print(f'Error verificando bucket: {e}')
            raise


def upload_report(local_path, s3_key):
    try:
        s3_client.upload_file(local_path, BUCKET_NAME, s3_key)
        print(f'Subido: {s3_key}')
        return True
    except botocore.exceptions.ClientError as e:
        print(f'Error subiendo {local_path}: {e}')
        return False


def upload_suite_reports(suite_name, reports_dir):
    valid_exts = VALID_EXTENSIONS.get(suite_name, [])
    uploaded = 0
    skipped = 0

    if not os.path.exists(reports_dir):
        print(f'Directorio no encontrado: {reports_dir}')
        return uploaded, skipped

    for filename in os.listdir(reports_dir):
        ext = os.path.splitext(filename)[1].lower()
        if ext not in valid_exts:
            skipped += 1
            continue

        local_path = os.path.join(reports_dir, filename)
        if not os.path.isfile(local_path):
            continue

        s3_key = f'{suite_name}/{DATE_PREFIX}/{filename}'
        success = upload_report(local_path, s3_key)
        if success:
            uploaded += 1

    return uploaded, skipped


def list_uploaded_reports():
    try:
        response = s3_client.list_objects_v2(Bucket=BUCKET_NAME)
        objects = response.get('Contents', [])
        if not objects:
            print('  (sin archivos en el bucket)')
            return

        for obj in objects:
            size_kb = obj['Size'] / 1024
            print(f"{obj['Key']} ({size_kb:.1f} KB)")
    except botocore.exceptions.ClientError as e:
        print(f'Error listando objetos: {e}')


if __name__ == "__main__":
    print("=" * 55)
    print("  QA Reports Upload — coffee-cart")
    print(f"  Fecha: {DATE_PREFIX}")
    print("=" * 55)

    ensure_bucket_exists(BUCKET_NAME)
    print()

    total_uploaded = 0
    total_skipped = 0

    for suite, reports_dir in REPORTS.items():
        print(f'Suite: {suite.upper()} ({reports_dir})')
        uploaded, skipped = upload_suite_reports(suite, reports_dir)
        print(f'   Subidos: {uploaded} | Ignorados: {skipped}')
        total_uploaded += uploaded
        total_skipped += skipped
        print()

    print("=" * 55)
    print(f'  Total subidos : {total_uploaded}')
    print(f'  Total ignorados: {total_skipped}')
    print()
    print("Contenido del bucket:")
    list_uploaded_reports()
    print("=" * 55)