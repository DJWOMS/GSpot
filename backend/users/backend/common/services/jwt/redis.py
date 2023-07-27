from config.settings import redis_config
from utils.db.redis_client import RedisAccessClient, RedisClient, RedisRefreshClient


class RedisToken():
    @staticmethod
    def add_token_to_redis(redis_client: RedisClient, token: str, value: dict):
        redis_client.add_token(token=token, value=value)


class RedisAccessToken(RedisToken):
    redis_access_client = RedisAccessClient(
        host=redis_config.REDIS_SHARED_HOST,
        port=redis_config.REDIS_SHARED_PORT,
        db=redis_config.REDIS_ACCESS_DB,
        password=redis_config.REDIS_SHARED_PASSWORD,
    )

    @classmethod
    def add_access_to_redis(cls, token: str, value: dict):
        cls.add_token_to_redis(redis_client=cls.redis_access_client, token=token, value=value)
    
    def get_access_data(self, token: str) -> dict | None:
        return self.redis_access_client.is_token_exist(token)


class RedisBanRefreshToken(RedisToken):
    redis_refresh_client = RedisRefreshClient(
        host=redis_config.REDIS_SHARED_HOST,
        port=redis_config.REDIS_SHARED_PORT,
        db=redis_config.REDIS_REFRESH_DB,
        password=redis_config.REDIS_SHARED_PASSWORD,
    )

    @classmethod
    def add_refresh_to_redis(cls, token: str, value: dict = None):
        cls.add_token_to_redis(redis_client=cls.redis_refresh_client, token=token, value=value)
    
    def get_refresh_data(self, token: str) -> dict | None:
        return self.redis_refresh_client.is_token_exist(token)
