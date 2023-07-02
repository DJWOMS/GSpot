from abc import ABCMeta

from django.contrib.auth.models import AbstractUser
from rest_framework.exceptions import ValidationError


class AbstractUserVerify:
    """Common abstract class for user verification"""

    def verify(self, user: AbstractUser) -> bool:
        """check user verification by condition"""
        raise NotImplementedError


class AbstractUserValidation(AbstractUserVerify, metaclass=ABCMeta):
    """Common abstract class for user validation"""

    exception: ValidationError

    def validate(self, user: AbstractUser):
        """Raise error if user has not passed verification"""
        raise NotImplementedError


class BaseUserValidation(AbstractUserValidation):
    exception = ValidationError
    error_message = "ValidationError"

    def __init__(self, message=""):
        if message:
            self.error_message = message

    def verify(self, user: AbstractUser) -> bool:
        raise NotImplementedError

    def validate(self, user):
        if not self.verify(user):
            raise self.exception(self.error_message)
