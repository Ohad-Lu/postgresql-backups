from os import environ
from dotenv import load_dotenv

load_dotenv()


class Config:
    def __init__(self) -> None:
        self.database_connection_string = environ["DATABASE_CONNECTION_STRING"]
        self.celery_connection_string = environ["CELERY_CONNECTION_STRING"]


config = Config()
