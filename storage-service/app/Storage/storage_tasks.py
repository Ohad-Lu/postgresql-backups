from celery import Celery
from app.Config import config
import boto3
from botocore.exceptions import ClientError

app = Celery("storage_tasks", broker=config.celery_broker_uri)


@app.task
def upload_to_aws(aws_bucket_name, aws_access_key_id, aws_secret_access_id, filename):
    source_bucket = boto3.client(
        "s3",
        aws_access_key_id=config.aws_access_key_id,
        aws_secret_access_key=config.aws_secret_access_id,
        endpoint_url=config.s3_endpoint_url,
        verify=False,
    )
    target_bucket = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_id,
        endpoint_url="http://127.0.0.1:9000",
        verify=False,
    )
    # s3 = boto3.resource("s3")
    copy_source = {"Bucket": "backups", "Key": filename}
    source_bucket.copy(copy_source, aws_bucket_name, filename)
