import gzip
from sh import pg_dump
from celery import Celery
from app.Config import config

app = Celery('tasks', broker=config.celery_broker_uri)
@app.task
def backup_db_task(db_hostname, db_username, db_database_name, db_password, dest_filename):
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
    return "success"