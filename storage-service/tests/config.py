from app.api import app
from dotenv import load_dotenv
from os import environ

load_dotenv()

item_json = {
    "id": 0,
    "name": "aws-test",
    "type": "s3",
    "s3_endpoint_url": environ["PYTEST_S3_ENDPOINT_URL"],
    "s3_bucket_name": environ["PYTEST_S3_BUCKET_NAME"],
    "s3_secret_access_key": environ["PYTEST_S3_SECRET_ACCESS_KEY"],
    "s3_access_key_id": environ["PYTEST_S3_ACCESS_KEY_ID"],
}

prefix = "/storages"
app = app

filename = "file.gz"
