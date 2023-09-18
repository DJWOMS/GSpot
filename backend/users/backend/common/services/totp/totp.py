import uuid

from base.models import BaseAbstractUser
from base.tokens.totp import BaseTOTPToken
from common.services.email_delivery.email import EmailDelivery
from config.settings import redis_config
from rest_framework import serializers
from utils.broker.message import (
    AdminActivationMessage,
    CustomerActivationMessage,
    DevelopActivationMessage,
)
from utils.db.redis_client import RedisClient, RedisTotpClient


class TOTPToken(BaseTOTPToken):
    redis: RedisClient = RedisTotpClient(
        host=redis_config.REDIS_LOCAL_HOST,
        port=redis_config.REDIS_LOCAL_PORT,
        db=redis_config.REDIS_TOTP_DB,
        password=redis_config.REDIS_LOCAL_PASSWORD,
    )

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
        messages = {
            'administrator': AdminActivationMessage,
            'customer': CustomerActivationMessage,
            'developer': DevelopActivationMessage,
        }
        user_role = user._meta.app_label
        message = messages.get(user_role)
        rabbitmq_message = message(totp=totp, user=user)
        EmailDelivery().send_email(message=rabbitmq_message)

    def check_totp(self, totp: str):
        data = self.redis.is_token_exist(totp)
        if not data:
            raise serializers.ValidationError("Current TOTP is not exists.")
        return data
