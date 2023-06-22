from pydantic import BaseSettings


class RedisConfig(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int

    @property
    def url(self):
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}/'


redis_data = RedisConfig()


CELERY_BROKER_URL = redis_data.url + '0'

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': redis_data.url + '0',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    },
}
