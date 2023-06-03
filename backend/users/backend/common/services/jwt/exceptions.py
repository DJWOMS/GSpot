from django.core.exceptions import ValidationError


class TokenExpired(ValidationError):
    pass


class TokenInvalid(ValidationError):
    pass


class PayloadError(ValidationError):
    pass
