from celery import Celery
from app.Config import config
import boto3
from botocore.exceptions import ClientError

app = Celery("storage_tasks", broker=config.celery_broker_uri)


@app.task
def upload_to_aws(aws_bucket_name, aws_access_key_id, aws_secret_access_id, filename):
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_id,
        endpoint_url="http://127.0.0.1:9000",
        verify=False,
    )
    try:
        response = s3_client.upload_file(filename, aws_bucket_name, filename)
    except ClientError as e:
        return False
    return True
