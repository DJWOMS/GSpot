from pydantic import BaseSettings
import os


class RedisConfig(BaseSettings):
    REDIS_PORT: str = os.environ.get('MONGO_PORTS')
    REDIS_HOST: str = os.environ.get('MONGO_HOST')

    @property
    def url(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"


redis_config = RedisConfig()
