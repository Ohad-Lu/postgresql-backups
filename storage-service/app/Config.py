from os import environ
from dotenv import load_dotenv
from app.Storage.StorageModel import Storage

load_dotenv()


class Config:
    def __init__(self) -> None:
        self.database_connection_string = environ["DATABASE_CONNECTION_STRING"]
        self.celery_broker_uri = environ["CELERY_BROKER_URI"]
        self.celery_queue_name = environ["CELERY_QUEUE_NAME"]

        self.backups_bucket = Storage(
            type="s3",
            name="backups_bucket",
            s3_endpoint_url=environ["BACKUPS_BUCKET_ENDPOINT_URL"],
            s3_access_key_id=environ["BACKUPS_BUCKET_ACCESS_KEY_ID"],
            s3_bucket_name=environ["BACKUPS_BUCKET_NAME"],
            s3_secret_access_key=environ["BACKUPS_BUCKET_SECRET_ACCESS_KEY"],
        )


config = Config()
