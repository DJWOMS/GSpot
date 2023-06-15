import uuid

from base.models import BaseAbstractUser
from base.tokens.totp import BaseTOTPToken
from utils.db.redis_client import RedisTotpClient
from utils.broker.rabbitmq import RabbitMQ
from utils.broker.message import DevTOTPTokenMessage


class TOTPToken(BaseTOTPToken):
    def send_totp(self, user: BaseAbstractUser):
        totp = self.generate_totp()
        self.add_to_redis(totp, user)
        self.send_to_channels(totp)

    @staticmethod
    def generate_totp() -> str:
        return str(uuid.uuid4())

    def add_to_redis(self, totp: str, user: BaseAbstractUser):
        redis_client = RedisTotpClient()
        value = {
            "user_id": str(self.user.id),
            "role": user._meta.app_label,
        }
        redis_client.add_token(token=totp, value=value)

    @staticmethod
    def send_to_channels(totp: str):
        with RabbitMQ() as rabbit:
            message = {'totp': totp}
            totp_token_message = DevTOTPTokenMessage()
            totp_token_message.message = message
            rabbit.send_message(totp_token_message)
