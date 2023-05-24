from base.validators import BaseUserValidation
from common.permissions.verifiers import IsActiveUserVerify, NotBannedUserVerify


class ActiveUserValidator(IsActiveUserVerify, BaseUserValidation):
    """User Active Verification"""


class BannedUserValidatorVerify(NotBannedUserVerify, BaseUserValidation):
    """Banned User Verification"""
