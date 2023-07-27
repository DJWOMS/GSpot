import time

from base.exceptions import UserBanned, UserInActive
from base.models import BaseAbstractUser
from base.tokens.token import BaseToken
from common.services.jwt.exceptions import PayloadError, TokenExpired
from common.services.jwt.mixins import JWTMixin
from common.services.jwt.redis import RedisAccessToken, RedisBanRefreshToken
from common.services.jwt.users_payload import PayloadFactory
from django.conf import settings
from django.utils import timezone


class Token(BaseToken, JWTMixin):
    @staticmethod
    def validate_user(user: BaseAbstractUser):
        if user.is_active is not True:
            raise UserInActive("Пользователь не активный")
        elif user.is_banned is not False:
            raise UserBanned("Пользователь заблокирован")

    @staticmethod
    def validate_payload_data(data: dict):
        required_fields = ["user_id", "role"]
        for field in required_fields:
            if field not in data:
                raise PayloadError(f"Payload must contain '{field}'")

    @staticmethod
    def get_default_access_payload() -> dict:
        iat = timezone.localtime()
        exp = iat + settings.ACCESS_TOKEN_LIFETIME
        default_payload = {
            "iat": int(iat.timestamp()),
            "exp": int(exp.timestamp()),
        }
        return default_payload

    @staticmethod
    def get_default_refresh_payload() -> dict:
        iat = timezone.localtime()
        exp = iat + settings.REFRESH_TOKEN_LIFETIME
        default_payload = {
            "iat": int(iat.timestamp()),
            "exp": int(exp.timestamp()),
        }
        return default_payload

    def generate_tokens(self, data: dict) -> dict:
        access_token = self.generate_access_token(data)
        refresh_token = self.generate_refresh_token(data)
        return {"access": access_token, "refresh": refresh_token}

    def generate_access_token(self, data: dict = None) -> str:
        data = data if data is not None else {}
        self.validate_payload_data(data)
        default_payload = self.get_default_access_payload()
        redis_payload = {
            **data,
        }
        payload = {
            "token_type": "access",
            **default_payload,
        }
        access_token = self._encode(payload)
        RedisAccessToken.add_access_to_redis(token=access_token, value=redis_payload)
        return access_token

    def generate_refresh_token(self, data: dict) -> str:
        self.validate_payload_data(data)
        default_payload = self.get_default_refresh_payload()
        payload = {
            "token_type": "refresh",
            "user_id": data["user_id"],
            "role": data["role"],
            **default_payload,
        }
        refresh_token = self._encode(payload)
        return refresh_token

    def generate_tokens_for_user(self, user: BaseAbstractUser) -> dict:
        self.validate_user(user)
        access_token = self.generate_access_token_for_user(user)
        refresh_token = self.generate_refresh_token_for_user(user)
        return {"access": access_token, "refresh": refresh_token}

    def generate_access_token_for_user(self, user: BaseAbstractUser) -> str:
        self.validate_user(user)
        user_payload = self.get_user_payload(user)
        default_payload = self.get_default_access_payload()
        redis_payload = {
            **user_payload,
        }
        payload = {
            "token_type": "access",
            **default_payload,
        }
        access_token = self._encode(payload)
        RedisAccessToken.add_access_to_redis(token=access_token, value=redis_payload)
        return access_token

    def generate_refresh_token_for_user(self, user: BaseAbstractUser) -> str:
        self.validate_user(user)
        default_payload = self.get_default_refresh_payload()
        payload = {
            "token_type": "refresh",
            "user_id": str(user.id),
            "role": user._meta.app_label,
            **default_payload,
        }
        refresh_token = self._encode(payload)

        return refresh_token

    @staticmethod
    def get_user_payload(user: BaseAbstractUser) -> dict:
        factory = PayloadFactory()
        return factory.create_payload(user)

    def check_token(self, token: str) -> bool:
        self.check_exp(token)
        self.check_signature(token)
        return True

    def check_exp(self, token: str) -> int:
        exp_left = self.check_exp_left(token)
        if exp_left == 0:
            raise TokenExpired("Token is expired")
        else:
            return exp_left

    def check_exp_left(self, token: str) -> int:
        try:
            decoded_token = self._decode(token)
            now = int(time.time())
            exp = decoded_token["exp"]
            if exp > now:
                return exp - now
        except TokenExpired:
            return 0

    def check_signature(self, token: str) -> None:
        self._decode(token)

    # for backward compatibility
    redis_refresh_client = RedisBanRefreshToken.redis_refresh_client
    add_refresh_to_redis = RedisBanRefreshToken().add_refresh_to_redis
    get_access_data = RedisAccessToken().get_access_data
    get_refresh_data = RedisBanRefreshToken().get_refresh_data
