import os
import time

from celery import Celery

from config import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery(__name__)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()


# CHEK
@app.task
def debug_task():
    time.sleep(1)
    print('HELLO CELERY!!!')
