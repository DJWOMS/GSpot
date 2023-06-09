import redis
from config.settings import redis_config


class RedisClient:
    _prefix = ''

    def __init__(self, db: int):
        host = redis_config.REDIS_HOST
        port = redis_config.REDIS_PORT
        password = redis_config.REDIS_PASSWORD
        self.__redis_client = redis.StrictRedis(host=host, port=port, db=db, password=password)

    @property
    def conn(self):
        return self.__redis_client

    def get(self, name: str) -> str | None:
        return self.conn.get(name)

    def put(self, name: str, value: str, ttl: int) -> None:
        self.conn.set(name=name, value=value, ex=ttl)

    def is_token_exist(self, token: str) -> bool:
        if self.get(token):
            return True

        return False

    def add_token(self, token: str, ttl: int, prefix: bool = False):
        key = f'{self._prefix}:{token}' if prefix else token
        self.put(name=key, value=token, ttl=ttl)


class RedisAccessClient(RedisClient):
    _prefix = 'access'

    def __init__(self):
        db = redis_config.REDIS_ACCESS_DB
        super().__init__(db)


class RedisRefreshClient(RedisClient):
    _prefix = 'refresh'

    def __init__(self):
        db = redis_config.REDIS_REFRESH_DB
        super().__init__(db)


class RedisTotpClient(RedisClient):
    _prefix = 'totp'

    def __init__(self):
        db = redis_config.REDIS_TOTP_DB
        super().__init__(db)


redis_access_client = RedisAccessClient()
redis_refresh_client = RedisRefreshClient()
redis_totp_client = RedisTotpClient()
