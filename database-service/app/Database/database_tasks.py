import gzip
from sh import pg_dump
from celery import Celery

app = Celery('tasks', broker='pyamqp://guest@localhost//')
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