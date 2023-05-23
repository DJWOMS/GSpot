from base.validators import BaseUserValidation
from common.permissions.exceptions import NotActiveUserError, BannedUserError
from common.permissions.verifiers import IsActiveUserVerify, NotBannedUserVerify


class ActiveUserValidator(IsActiveUserVerify, BaseUserValidation):
    """User Active Verification"""

    exception = NotActiveUserError


class BannedUserValidatorVerify(NotBannedUserVerify, BaseUserValidation):
    """Banned User Verification"""

    exception = BannedUserError
