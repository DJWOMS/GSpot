import redis
from config.settings import redis_config


class RedisClient:
    def __init__(self, host: str, port: int, db: int, password: str):
        self.__redis_client = redis.StrictRedis(host=host, port=port, db=db, passsword=password)

    @property
    def client(self):
        return self.__redis_client


class RedisAccessClient(RedisClient):
    def __init__(self):
        host = redis_config.REDIS_HOST
        port = redis_config.REDIS_PORT
        db = redis_config.REDIS_ACCESS_DB
        password = redis_config.REDIS_PASSWORD
        super().__init__(host, port, db, password)


class RedisRefreshClient(RedisClient):
    def __init__(self):
        host = redis_config.REDIS_HOST
        port = redis_config.REDIS_PORT
        db = redis_config.REDIS_REFRESH_DB
        password = redis_config.REDIS_PASSWORD
        super().__init__(host, port, db, password)

