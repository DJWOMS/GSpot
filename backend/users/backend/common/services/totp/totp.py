import uuid

from rest_framework import serializers

from config.settings import redis_config
from base.models import BaseAbstractUser
from base.tokens.totp import BaseTOTPToken
from utils.broker.message import TOTPTokenMessage, BaseMessage
from utils.broker.rabbitmq import RabbitMQ
from utils.db.redis_client import RedisTotpClient, RedisClient
from common.services.totp.model_factory import db_model_factory


class TOTPToken(BaseTOTPToken):
    redis: RedisClient = RedisTotpClient(
        host=redis_config.REDIS_LOCAL_HOST,
        port=redis_config.REDIS_LOCAL_PORT,
        db=redis_config.REDIS_TOTP_DB,
        password=redis_config.REDIS_LOCAL_PASSWORD,
    )
    rabbitmq = RabbitMQ()
    message: BaseMessage = TOTPTokenMessage

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
            rabbitmq_message = self.message(message)
            rabbit.send_message(rabbitmq_message)

    def check_totp(self, totp: str):
        data = self.redis.is_token_exist(totp)
        if not data:
            raise serializers.ValidationError('Current TOTP is not exists.')
        return data
