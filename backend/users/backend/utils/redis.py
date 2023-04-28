import redis
from config.settings import redis_config


class RedisValidateToken:
    def __int__(self):
        self.redis_storage = redis.StrictRedis(host=redis_config.REDIS_HOST,
                                               port=redis_config.REDIS_PORT,
                                               db=redis_config.REDIS_DB,
                                               password=redis_config.REDIS_PASSWORD)

    def check_token_in_redis(self, token: str):
        pass

    def add_token_in_redis(self, token: str, ttl: float):
        pass

    def check_token_in_black_list(self, token: str):
        pass

    def add_token_in_black_list(self, token: str, ttl: float):
        pass

