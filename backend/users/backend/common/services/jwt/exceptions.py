from rest_framework.exceptions import ValidationError, AuthenticationFailed


class TokenExpired(ValidationError):
    pass


class TokenInvalid(ValidationError):
    pass


class PayloadError(ValidationError):
    pass


class UnauthorizedUserError(AuthenticationFailed):
    pass


class TokenBannedError(AuthenticationFailed):
    pass
