from pydantic import BaseSettings
import os


class DatabaseConfig(BaseSettings):
    port: str = os.environ.get('MONGO_PORTS')
    host: str = os.environ.get('MONGO_HOST')
    user: str = os.environ.get('MONGO_INITDB_ROOT_USERNAME')
    password: str = os.environ.get('MONGO_INITDB_ROOT_PASSWORD')
    db: str = os.environ.get('MONGO_INITDB_DATABASE')

    @property
    def url(self):
        return f'mongodb://{self.user}:{self.password}@{self.host}/{self.db}?authSource=admin'


db_config = DatabaseConfig()
