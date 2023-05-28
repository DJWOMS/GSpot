from pydantic import BaseSettings


class DataBaseDatas(BaseSettings):
    POSTGRES_PASSWORD: str
    POSTGRES_DB: str
    POSTGRES_USER: str
    POSTGRES_PORT: int
    POSTGRES_HOST: str

    @property
    def url(self):
        return (
            f'postgresql://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@'
            f'{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'
        )


db_datas_config = DataBaseDatas()


class RedisDatas(BaseSettings):
    REDIS_HOST: str
    REDIS_PORT: int

    @property
    def url(self):
        return f'redis://{self.REDIS_HOST}:{self.REDIS_PORT}/'


redis_datas = RedisDatas()


class RollbarAccessToken(BaseSettings):
    ROLLBAR_ACCESS_TOKEN: str

    @property
    def r_token(self):
        return self.ROLLBAR_ACCESS_TOKEN


rollbar_token = RollbarAccessToken()


class SecretKey(BaseSettings):
    SECRET_KEY: str

    @property
    def key(self):
        return self.SECRET_KEY


secret_key = SecretKey()


class JwtSecretKey(BaseSettings):
    JWT_SECRET_KEY: str

    @property
    def js_key(self):
        return self.JWT_SECRET_KEY


jwt_secret_key = JwtSecretKey()


class DebugValue(BaseSettings):
    DEBUG: bool = True


debug_value = DebugValue()


class AllowedHostsValue(BaseSettings):
    ALLOWED_HOSTS: str

    @property
    def alloved_host_value(self):
        return self.ALLOWED_HOSTS.split(',')


allowed_host = AllowedHostsValue()
