from celery import Celery
from app.Config import config
import boto3

app = Celery(config.celery_queue_name, broker=config.celery_broker_uri)


@app.task
def upload_to_aws(
    s3_bucket_name, s3_access_key_id, s3_secret_access_id, s3_endpoint_url, filename
):
    src_client = get_bucket(
        aws_access_key_id=config.aws_secret_access_id,
        aws_secret_access_id=config.aws_secret_access_id,
        s3_endpoint_url=config.s3_endpoint_url,
    )
    dst_client = get_bucket(
        aws_access_key_id=s3_access_key_id,
        aws_secret_access_id=s3_secret_access_id,
        s3_endpoint_url=s3_endpoint_url,
    )
    copy(
        src_client=src_client,
        src_bucket=config.backups_bucket_name,
        src_file=filename,
        dst_client=dst_client,
        dst_bucket=s3_bucket_name,
        dst_file=filename,
    )


def get_bucket(aws_access_key_id, aws_secret_access_id, s3_endpoint_url):
    return boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_id,
        endpoint_url=s3_endpoint_url,
        verify="https" in s3_endpoint_url,
    )


def download(client: boto3.client("s3"), bucket_name, filename):
    client.download_file(bucket_name, filename, filename)
    return filename


def upload(client: boto3.client("s3"), bucket_name, src_file, dst_file):
    client.upload_file(src_file, bucket_name, dst_file)
    return f"{bucket_name}/{dst_file}"


def copy(
    src_client: boto3.client("s3"),
    src_bucket,
    src_file,
    dst_client: boto3.client("s3"),
    dst_bucket,
    dst_file,
):
    downloaded_file_path = download(src_client, src_bucket, src_file)

    return upload(
        client=dst_client,
        bucket=dst_bucket,
        src_file=downloaded_file_path,
        dst_file=dst_file,
    )
