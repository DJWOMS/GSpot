from base.exceptions import AuthenticationFailed


class TokenExpired(AuthenticationFailed):
    pass


class TokenInvalid(AuthenticationFailed):
    pass


class PayloadError(AuthenticationFailed):
    pass
