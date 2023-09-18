from typing import final

import jwt
from common.services.jwt.exceptions import TokenExpired, TokenInvalid
from django.conf import settings
from jwt.exceptions import ExpiredSignatureError


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
        except ExpiredSignatureError:
            raise TokenExpired("Token is expired")
        except Exception:
            raise TokenInvalid("%s is invalid token" % token)
