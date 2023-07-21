import os
import time

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
app = Celery(__name__)
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()


# CHEK
@app.task
def debug_task():
    time.sleep(1)
    print("!!!WELCOME TO THE CLUB, BUDDY!!!")
