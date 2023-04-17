from pydantic import BaseSettings
import os


class RabbitConfig(BaseSettings):
    port: str = os.environ.get('BROKER_PORTS')
    host: str = os.environ.get('BROKER_HOST')
    user: str = os.environ.get('BROKER_USER')
    password: str = os.environ.get('BROKER_PASSWORD')
    vhost: str = os.environ.get('BROKER_VHOST')

    @property
    def url(self):
        return f'amqp://{self.user}:{self.password}@{self.host}:{self.port}/{self.vhost}'


rabbitmq_config = RabbitConfig()
