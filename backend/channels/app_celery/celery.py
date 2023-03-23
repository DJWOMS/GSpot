from celery import Celery


app_celery = Celery("app_celery")


@app_celery.task
def ping():
    return "pong"
