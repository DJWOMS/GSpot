import uuid

from django.conf import settings

from base.models import BaseAbstractUser
from base.tokens.totp import BaseTOTPToken
from utils.broker.message import DevTOTPTokenMessage, BaseMessage
from utils.broker.rabbitmq import RabbitMQ
from utils.db.redis_client import RedisTotpClient, RedisClient


class TOTPToken(BaseTOTPToken):
    redis: RedisClient = RedisTotpClient()
    rabbitmq = RabbitMQ()
    message: BaseMessage = DevTOTPTokenMessage

    def send_totp(self, user: BaseAbstractUser):
        totp = self.generate_totp()
        self.add_to_redis(totp, user)
        self.send_to_channels(totp, user.email)

    @staticmethod
    def generate_totp() -> str:
        return str(uuid.uuid4())

    def add_to_redis(self, totp: str, user: BaseAbstractUser):
        value = {
            "user_id": str(user.id),
            "role": user._meta.app_label,
        }
        self.redis.add_token(token=totp, value=value)

    def send_to_channels(self, totp: str, email: str):
        with self.rabbitmq as rabbit:
            message = {'totp': totp, 'email': email}
            rabbitmq_message = self.message(
                settings.TOTP_EXCHANGE_NAME, settings.TOTP_ROUTING_KEY, message
            )
            rabbit.send_message(rabbitmq_message)

    def check_totp(self, totp: str):
        pass
