from rest_framework import status
from rest_framework.exceptions import ValidationError


class TokenExpired(Exception):
    pass


class TokenInvalid(Exception):
    pass


class PayloadError(Exception):
    pass


class UnauthorizedUserError(ValidationError):
    ValidationError.status_code = status.HTTP_401_UNAUTHORIZED


class TokenBannedError(ValidationError):
    ValidationError.status_code = status.HTTP_401_UNAUTHORIZED
