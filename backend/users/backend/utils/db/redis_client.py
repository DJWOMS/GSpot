import redis
from config.settings import redis_config
from config.settings.jwt import ACCESS_TOKEN_LIFETIME, REFRESH_TOKEN_LIFETIME


class RedisClient:
    _prefix = 'basic'
    _ttl = 300

    def __init__(self, db: int):
        host = redis_config.REDIS_HOST
        port = redis_config.REDIS_PORT
        password = redis_config.REDIS_PASSWORD
        self.__redis_client = redis.StrictRedis(host=host, port=port, db=db, password=password)

    @property
    def conn(self):
        return self.__redis_client

    def __get(self, name: str) -> str | None:
        return self.conn.get(name)

    def __put(self, name: str, value: dict, ttl: int) -> None:
        self.conn.set(name=name, value=value, ex=ttl)

    def is_token_exist(self, token: str, prefix: bool = True) -> str | None:
        key = f'{self._prefix}:{token}' if prefix else token
        return self.__get(key)

    def add_token(self, token: str, value: dict = None, ttl: int = _ttl, prefix: bool = True):
        key = f'{self._prefix}:{token}' if prefix else token
        value = value if value is not None else dict
        self.__put(name=key, value=value, ttl=ttl)


class RedisAccessClient(RedisClient):
    _prefix = redis_config.REDIS_ACCESS_PREFIX
    _ttl = ACCESS_TOKEN_LIFETIME

    def __init__(self):
        db = redis_config.REDIS_ACCESS_DB
        super().__init__(db)


class RedisRefreshClient(RedisClient):
    _prefix = redis_config.REDIS_REFRESH_PREFIX
    _ttl = REFRESH_TOKEN_LIFETIME

    def __init__(self):
        db = redis_config.REDIS_REFRESH_DB
        super().__init__(db)


class RedisTotpClient(RedisClient):
    _prefix = redis_config.REDIS_TOTP_PREFIX

    def __init__(self):
        db = redis_config.REDIS_TOTP_DB
        super().__init__(db)


redis_access_client = RedisAccessClient()
redis_refresh_client = RedisRefreshClient()
redis_totp_client = RedisTotpClient()
