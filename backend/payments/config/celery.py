import os
import time

from celery import Celery
from celery.schedules import crontab
from config import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
app = Celery(__name__)
app.config_from_object('django.conf:settings', namespace='CELERY')
app.conf.broker_url = settings.CELERY_BROKER_URL
app.autodiscover_tasks()

import django  # noqa: E402

django.setup()
from apps.payment_accounts.models import Owner  # noqa: E402

PAYOUT_DAY = Owner.objects.first().payout_day_of_month


# CHEK
@app.task
def debug_task():
    time.sleep(1)
    print('HELLO CELERY!!!')


app.conf.beat_schedule = {
    'make_auto_payout': {
        'task': 'apps.payment_accounts.tasks.make_auto_payout',
        'schedule': crontab(day_of_month=PAYOUT_DAY),
    },
}
