import time

from django.conf import settings
from django.utils import timezone

from base.token import BaseToken
from common.services.jwt.exceptions import TokenExpired, PayloadError
from common.services.jwt.mixins import JWTMixin


class Token(BaseToken, JWTMixin):
    def generate_access_token(self, data: dict = {}) -> str:
        self._validate_payload_data(data)
        iat = timezone.localtime()
        exp = iat + settings.ACCESS_TOKEN_LIFETIME
        payload = {
            "token_type": "access",
            "iat": int(iat.timestamp()),
            "exp": int(exp.timestamp()),
            **data,
        }
        access_token = self._encode(payload)
        return access_token

    def _validate_payload_data(self, data: dict) -> None:
        required_fields = ['user_id', 'role']
        for field in required_fields:
            if field not in data:
                raise PayloadError(f"Payload must contain - {field}")

    def generate_refresh_token(self, user_id: str, role: str) -> str:
        iat = timezone.localtime()
        exp = iat + settings.REFRESH_TOKEN_LIFETIME
        payload = {
            "token_type": "refresh",
            "iat": int(iat.timestamp()),
            "exp": int(exp.timestamp()),
            "user_id": user_id,
            "role": role,
        }
        refresh_token = self._encode(payload)
        return refresh_token

    def generate_tokens(self, data: dict) -> dict:
        access_token = self.generate_access_token(data)
        refresh_token = self.generate_refresh_token(data.id, data.role)
        return {"access": access_token, "refresh": refresh_token}

    def check_token(self, token: str) -> bool:
        self._check_exp(token)
        self._check_signature(token)
        return True

    def _check_exp(self, token: str) -> int:
        exp_left = self.check_exp_left(token)
        if exp_left == 0:
            raise TokenExpired()
        else:
            return exp_left

    def check_exp_left(self, token: str) -> int:
        decoded_token = self._decode(token)
        now = int(time.time())
        exp = decoded_token['exp']

        if exp > now:
            return exp - now
        else:
            return 0

    def _check_signature(self, token: str) -> None:
        self._decode(token)
