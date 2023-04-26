from base.permissions import VerificationError, BaseUserVerification


class NotActiveUserError(VerificationError):
    pass


class ActiveUserVerify(BaseUserVerification):
    """User Active Verification"""

    exception = NotActiveUserError
    message = 'user not active'

    def _condition(self, user):
        return not user.is_active


class BannedUserError(VerificationError):
    pass


class BannedUserVerify(BaseUserVerification):
    """Banned User Verification"""

    exception = BaseUserVerification
    message = 'user is banned'

    def _condition(self, user):
        return user.is_banned
