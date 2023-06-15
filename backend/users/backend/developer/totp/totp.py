import uuid

from base.models import BaseAbstractUser
from base.tokens.totp import BaseTOTPToken
from utils.db.redis_client import RedisTotpClient


class TOTPToken(BaseTOTPToken):
    @staticmethod
    def generate_totp() -> str:
        totp = str(uuid.uuid4())
        return totp

    def add_to_redis(self, totp: str, user: BaseAbstractUser):
        redis_client = RedisTotpClient()
        value = {
            "user_id": str(self.user.id),
            "role": user._meta.app_label,
        }
        redis_client.add_token(token=totp, value=value)
