from datetime import date

from celery import current_app as app
from celery.schedules import crontab
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Owner
from .tasks import make_auto_payout


@receiver(post_save, sender=Owner)
def update_celery_schedule(sender, instance, **kwargs):
    try:
        payout_day = instance.payout_day_of_month
        print(f'--day--{payout_day}')
        task_name = 'make_auto_payout'
        if task_name in app.conf.beat_schedule:
            print(f'вот расписание {app.conf.beat_schedule}')
            del app.conf.beat_schedule[task_name]
        app.conf.beat_schedule[task_name] = {
            'task': 'apps.payment_accounts.tasks.make_auto_payout',
            'schedule': crontab(day_of_month=payout_day),
        }
        print(f'новое {app.conf.beat_schedule[task_name]}')
        current_date = date.today()
        if current_date.day == payout_day:
            make_auto_payout.apply_async()
    except Exception as error:
        return error
