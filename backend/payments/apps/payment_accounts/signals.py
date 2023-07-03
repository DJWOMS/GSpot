from datetime import date

import rollbar
from celery import current_app as app
from celery.exceptions import TaskError
from celery.schedules import crontab
from django.db.models.signals import pre_save
from django.dispatch import receiver

from .models import Owner
from .tasks import make_auto_payout


@receiver(pre_save, sender=Owner)
def update_auto_payout_schedule(instance, **kwargs):
    payout_day = instance.payout_day_of_month
    task_name = 'make_auto_payout'

    if task_name in app.conf.beat_schedule:
        del app.conf.beat_schedule[task_name]
    app.conf.beat_schedule[task_name] = {
        'task': 'apps.payment_accounts.tasks.make_auto_payout',
        'schedule': crontab(day_of_month=payout_day),
    }

    current_date = date.today()
    if current_date.day == payout_day:
        try:
            make_auto_payout.apply_async()
        except TaskError as error:
            rollbar.report_message(f'{error}', level='error')
