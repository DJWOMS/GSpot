from pydantic import BaseSettings


class RedisConfig(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: str

    @property
    def url(self):
        return f"redis://{self.REDIS_HOST}:{self.REDIS_PORT}/0"


redis_config = RedisConfig()
