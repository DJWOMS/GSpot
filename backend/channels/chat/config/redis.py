from pydantic import BaseSettings
import os


class RadisConfig(BaseSettings):
    host: str = os.environ.get('REDIS_HOST')
    port: str = os.environ.get('REDIS_PORT')

    @property
    def url(self):
        return f"redis://' + {self.host} + ':' + {self.port} + '/0"


radis_config = RadisConfig()
