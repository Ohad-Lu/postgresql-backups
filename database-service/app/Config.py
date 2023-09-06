""" get env vars """
from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self) -> None:
        self.database_connection_string = environ["DATABASE_CONNECTION_STRING"]
        self.celery_broker_uri = environ["CELERY_BROKER_URI"]
        self.s3_endpoint_url = environ["S3_ENDPOINT_URL"]
        self.backups_bucket_name = environ["BACKUPS_BUCKET_NAME"]
        self.aws_access_key_id = environ["AWS_ACCESS_KEY_ID"]
        self.aws_secret_access_id = environ["AWS_SECRET_ACCESS_ID"]


config = Config()
