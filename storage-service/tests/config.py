from app.api import app
from dotenv import load_dotenv
from os import environ

load_dotenv()

item_json = {
    "id": 0,
    "name": "aws-test",
    "type": "s3",
    "aws_bucket_name": environ["PYTEST_AWS_BUCKET_NAME"],
    "aws_secret_access_id": environ["PYTEST_AWS_SECRET_ACCESS_ID"],
    "aws_access_key_id": environ["PYTEST_AWS_ACCESS_KEY_ID"],
}

prefix = "/storages"
app = app

filename = "file.gz"
