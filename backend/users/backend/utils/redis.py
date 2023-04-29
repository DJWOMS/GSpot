import redis
from config.settings import redis_config
from redis_client import RedisClient


class RedisValidateToken:
    def is_access_token_exist(self, client: RedisClient, token: str) -> bool:
        pass

    def add_valid_token(self, client: RedisClient, token: str, ttl: int) -> None:
        pass

