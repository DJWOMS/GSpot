from rest_framework.exceptions import ValidationError


class VerificationError(ValidationError):
    """Common base class for all verification exceptions."""


class NotActiveUserError(VerificationError):
    """Not Active User Error"""


class BannedUserError(VerificationError):
    """Banned User Error"""
