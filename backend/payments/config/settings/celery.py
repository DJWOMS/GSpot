from config.settings.pydantic_files import redis_datas

CELERY_BROKER_URL = redis_datas.url + '0'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': redis_datas.url + '0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    },
}
