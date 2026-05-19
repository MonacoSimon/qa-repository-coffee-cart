import boto3
import botocore.exceptions

s3_client = boto3.client(
    's3',
    endpoint_url="${LOCALSTACK_URL:-http://localhost:4566}",       
    aws_access_key_id='test',                   
    aws_secret_access_key='test',               
    region_name='us-east-1'
)

bucket_name = 'qa-s3-auto-bucket'
file_name = 'auto-test.txt'
file_content = b'Esto es un archivo que sera subido por python y boto3 a un bucket'


def create_and_verify_bucket(bucket_name):
    try:
        s3_client.create_bucket(Bucket=bucket_name)
        response = s3_client.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        if bucket_name in buckets:
            print(f'Bucket "{bucket_name}" creado exitosamente.')
        else:
            print(f'Error: El bucket "{bucket_name}" no se creó correctamente.')
    except botocore.exceptions.ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == 'BucketAlreadyOwnedByYou':          
            print(f'Bucket "{bucket_name}" ya existe, continuando...')
        else:
            print(f'Error al crear el bucket: {e}')


def upload_and_verify_file(bucket_name, file_name, file_content):
    try:
        s3_client.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        objects = [obj['Key'] for obj in response.get('Contents', [])]
        if file_name in objects:
            print(f'Archivo "{file_name}" subido exitosamente al bucket "{bucket_name}".')
        else:
            print(f'Error: El archivo "{file_name}" no se subió correctamente.')
    except botocore.exceptions.ClientError as e:
        print(f'Error al subir el archivo: {e}')


def download_and_verify_file(bucket_name, file_name, original_content):
    try:
        response = s3_client.get_object(Bucket=bucket_name, Key=file_name)
        downloaded_content = response['Body'].read()
        if downloaded_content == original_content:
            print(f'Archivo "{file_name}" descargado correctamente y el contenido coincide.')
        else:
            print(f'Error: El contenido descargado no coincide con el original.')
    except botocore.exceptions.ClientError as e:
        print(f'Error al descargar el archivo: {e}')


if __name__ == "__main__":
    print("Iniciando proceso: creación de bucket, subida y verificación del archivo...")
    create_and_verify_bucket(bucket_name)
    upload_and_verify_file(bucket_name, file_name, file_content)
    download_and_verify_file(bucket_name, file_name, file_content)