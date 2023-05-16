from pydantic import BaseSettings
import os


class RedisConfig(BaseSettings):
    REDIS_PORT: str = os.environ.get('REDIS_PORT')
    REDIS_HOST: str = os.environ.get('REDIS_HOST')
    REDIS_DB: str = os.environ.get('REDIS_DB_NUMBER')

    @property
    def url(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/{self.REDIS_DB}"


redis_config = RedisConfig()