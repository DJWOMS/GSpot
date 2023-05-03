from typing import final

import jwt
from django.conf import settings

from common.services.jwt.exceptions import TokenInvalid


class JWTMixin:
    @final
    @staticmethod
    def _encode(payload: dict) -> str:
        return jwt.encode(payload, settings.SECRET_KEY, settings.ALGORITHM)

    @final
    @staticmethod
    def _decode(token: str) -> dict:
        try:
            return jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
        except Exception:
            raise TokenInvalid
