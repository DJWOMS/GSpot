import dj_database_url
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
            f'postgres://{self.POSTGRES_USER}:{self.POSTGRES_PASSWORD}@'
            f'{self.POSTGRES_HOST}:{self.POSTGRES_PORT}/{self.POSTGRES_DB}'
        )


db_datas_config = DataBaseDatas()


DATABASES = {'default': dj_database_url.config(default=db_datas_config.url)}