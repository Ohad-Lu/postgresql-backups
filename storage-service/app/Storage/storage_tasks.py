from celery import Celery
from app.Config import config

app = Celery("storage_tasks", broker=config.celery_broker_uri)


@app.task
def task(task_param):
    return "success"
