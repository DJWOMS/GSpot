import uuid
from base.models import BaseAbstractUser
from base.tokens.totp import BaseTOTPToken
from config.settings import redis_config
from utils.broker import message as message_broker
from utils.broker.rabbitmq import RabbitMQ
from utils.db.redis_client import RedisTotpClient, RedisClient


class TOTPToken(BaseTOTPToken):
    redis: RedisClient = RedisTotpClient(
        host=redis_config.REDIS_LOCAL_HOST,
        port=redis_config.REDIS_LOCAL_PORT,
        db=redis_config.REDIS_TOTP_DB,
        password=redis_config.REDIS_LOCAL_PASSWORD,
    )
    rabbitmq: RabbitMQ = RabbitMQ()

    def send_totp(self, user: BaseAbstractUser):
        totp = self.generate_totp()
        self.add_to_redis(totp, user)
        self.send_to_channels(totp, user)

    @staticmethod
    def generate_totp() -> str:
        return str(uuid.uuid4())

    def add_to_redis(self, totp: str, user: BaseAbstractUser):
        value = {
            "user_id": str(user.id),
            "role": user._meta.app_label,
        }
        self.redis.add_token(token=totp, value=value)

    def send_to_channels(self, totp: str, user: BaseAbstractUser):
        with self.rabbitmq as rabbit:
            if user._meta.app_label == 'administrator':
                message = message_broker.AdminActivationMessage
            elif user._meta.app_label == 'customer':
                message = message_broker.CustomerActivationMessage
            else:
                message = message_broker.DevelopActivationMessage
            rabbitmq_message = message(user=user, totp=totp)
            rabbit.send_message(rabbitmq_message)

    def check_totp(self, totp: str):
        pass
