from config.settings import env
import django_redis

REDIS_URL = env.str('REDIS')


CELERY_BROKER_URL = REDIS_URL + '0'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': REDIS_URL + '0'
    },
}
