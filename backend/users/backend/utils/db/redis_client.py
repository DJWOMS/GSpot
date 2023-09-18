import json
import os

import redis
from config.settings import redis_config


class RedisClient:
    _prefix = "basic"
    _ttl = 300

    def __init__(self, host: str or tuple, port: int or tuple, db: int, password: str):
        host = host if type(host) is not tuple else host[0]
        port = port if type(port) is not tuple else port[0]
        self.__redis_client = redis.StrictRedis(host=host, port=port, db=db, password=password)

    @property
    def conn(self):
        return self.__redis_client

    def __get(self, name: str) -> dict | None:
        value = self.conn.get(name)
        if value:
            return json.loads(value)

    def __put(self, name: str, value: dict, ttl: int) -> None:
        value_data = json.dumps(value)
        self.conn.set(name=name, value=value_data, ex=ttl)

    def is_token_exist(self, token: str, prefix: bool = True) -> dict | None:
        key = f"{self._prefix}:{token}" if prefix else token
        return self.__get(key)

    def add_token(self, token: str, value: dict = None, ttl: int = None, prefix: bool = True):
        key = f"{self._prefix}:{token}" if prefix else token
        ttl = ttl if ttl is not None else self._ttl
        value = value if value is not None else {"token": key}
        self.__put(name=key, value=value, ttl=ttl)


class RedisAccessClient(RedisClient):
    _prefix = redis_config.REDIS_ACCESS_PREFIX
    _ttl = int(os.environ["ACCESS_TOKEN_LIFETIME"])

    def __init__(self, host: str, port: int, db: int, password: str):
        super().__init__(host=host, port=port, db=db, password=password)


class RedisRefreshClient(RedisClient):
    _prefix = redis_config.REDIS_REFRESH_PREFIX
    _ttl = int(os.environ["REFRESH_TOKEN_LIFETIME"])

    def __init__(self, host: str, port: int, db: int, password: str):
        super().__init__(host=host, port=port, db=db, password=password)


class RedisTotpClient(RedisClient):
    _prefix = redis_config.REDIS_TOTP_PREFIX

    def __init__(self, host: str, port: int, db: int, password: str):
        super().__init__(host=host, port=port, db=db, password=password)
