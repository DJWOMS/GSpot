from config.settings import redis_config
from utils.db.redis_client import RedisAccessClient, RedisRefreshClient


class RedisAccessToken:
    client = RedisAccessClient(
        host=redis_config.REDIS_SHARED_HOST,
        port=redis_config.REDIS_SHARED_PORT,
        db=redis_config.REDIS_ACCESS_DB,
        password=redis_config.REDIS_SHARED_PASSWORD,
    )

    def add(self, token: str, value: dict):
        self.client.add_token(token=token, value=value)

    def get_data(self, token: str) -> dict | None:
        return self.client.is_token_exist(token)


class RedisBanRefreshToken:
    client = RedisRefreshClient(
        host=redis_config.REDIS_SHARED_HOST,
        port=redis_config.REDIS_SHARED_PORT,
        db=redis_config.REDIS_REFRESH_DB,
        password=redis_config.REDIS_SHARED_PASSWORD,
    )

    def ban(self, token: str, value: dict = None):
        self.client.add_token(token=token, value=value)

    def get_data(self, token: str) -> dict | None:
        return self.client.is_token_exist(token)
