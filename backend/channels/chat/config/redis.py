from pydantic import BaseSettings
<<<<<<< HEAD
import os


class RadisConfig(BaseSettings):
    host: str = os.environ.get('REDIS_HOST')
    port: str = os.environ.get('REDIS_PORT')

    @property
    def url(self):
        return f"redis://' + {self.host} + ':' + {self.port} + '/0"


radis_config = RadisConfig()
=======


class RedisConfig(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: str

    @property
    def url(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"


redis_config = RedisConfig()
>>>>>>> origin/channels
