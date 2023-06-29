from config.settings.base import env
# from celery.schedules import crontab
# from config.settings.business_settings import PAYOUT_DAY
# from apps.payment_accounts.utils.cache import get_payout_day
# DAY = get_payout_day()
# from apps.payment_accounts.models import Owner
#
# PAYOUT_DAY = Owner.objects.first().payout_day_of_month

CELERY_BROKER_URL = env.str('REDIS') + '0'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': env.str('REDIS') + '0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    },
}

# CELERY_BEAT_SCHEDULE = {
#     'make_auto_payout': {
#         'task': 'apps.payment_accounts.tasks.make_auto_payout',
#         'schedule': crontab(day_of_month=PAYOUT_DAY),
#     }
# }
