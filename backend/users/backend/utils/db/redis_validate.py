import redis
from config.settings import redis_config
from .redis_client import RedisClient


class RedisValidateToken:
    @staticmethod
    def is_token_exist(client: RedisClient, token: str) -> bool:
        if client.is_token_exist(token):
            return True

        return False

    @staticmethod
    def add_token(client: RedisClient, token: str, ttl: int, prefix: bool = False) -> None:
        client.add_token(token=token, ttl=ttl, prefix=prefix)
