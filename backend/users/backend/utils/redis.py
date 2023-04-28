from ..config.settings import base

import redis


class RedisValidateToken:
    def __int__(self):
        self.redis_storage = redis.StrictRedis(host=base.REDIS_HOST, port=base.REDIS_PORT, db=0)

    def validate_token(self, token):
        pass

    def add_blacklist_token(self, token):
        pass

