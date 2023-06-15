import uuid

from base.models import BaseAbstractUser
from base.tokens.totp import BaseTOTPToken
from utils.db.redis_client import RedisTotpClient


class TOTPToken(BaseTOTPToken):
    def send_totp(self, user: BaseAbstractUser):
        totp = self.generate_totp()
        self.add_to_redis(totp, user)

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
