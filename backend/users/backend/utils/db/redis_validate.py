import redis
from config.settings import redis_config
from .redis_client import RedisClient


class RedisValidateToken:
    @staticmethod
    def is_token_exist(client: RedisClient, token: str) -> bool:
        if client.conn.exists(token):
            return True

        return False

    @staticmethod
    def add_token(client: RedisClient, token: str, ttl: int, prefix: str or None = None) -> None:
        key = f'{prefix}:{token}' if prefix is not None else token
        client.conn.set(name=key, value=token, ex=ttl)

