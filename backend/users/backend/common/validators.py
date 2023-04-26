from base.validators import VerificationError, BaseUserVerification


class NotActiveUserError(VerificationError):
    message = 'not active user'


class ActiveUserVerify(BaseUserVerification):
    """User Active Verification"""

    exception = NotActiveUserError

    def _condition(self, user):
        return not user.is_active


class BannedUserError(VerificationError):
    message = 'user is  banned'


class BannedUserVerify(BaseUserVerification):
    """Banned User Verification"""

    exception = BannedUserError

    def _condition(self, user):
        return user.is_banned
