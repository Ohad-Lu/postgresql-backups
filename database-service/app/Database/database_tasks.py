import gzip
from sh import pg_dump
from celery import Celery
from app.Config import config
import boto3
from botocore.exceptions import ClientError

app = Celery("tasks", broker=config.celery_broker_uri)


@app.task
def backup_db_task(
    db_hostname, db_username, db_database_name, db_password, dest_filename
):
    with gzip.open(dest_filename, "wb") as f:
        pg_dump(
            "-h",
            db_hostname,
            "-U",
            db_username,
            db_database_name,
            _out=f,
            _env={"PGPASSWORD": db_password},
        )

    response = upload_to_aws_task(
        endpoint_url=config.s3_endpoint_url,
        aws_bucket_name=config.backups_bucket_name,
        aws_secret_access_id=config.aws_secret_access_id,
        aws_access_key_id=config.aws_access_key_id,
        filename=dest_filename,
    )
    return response


def upload_to_aws_task(
    endpoint_url, aws_bucket_name, aws_access_key_id, aws_secret_access_id, filename
):
    s3_client = boto3.client(
        "s3",
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_id,
        endpoint_url=endpoint_url,
        verify="https" in endpoint_url,
    )

    response = s3_client.upload_file(filename, aws_bucket_name, filename)

    return response
