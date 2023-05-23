from abc import ABCMeta
from typing import Type

from django.contrib.auth.models import AbstractUser
from common.permissions.exceptions import VerificationError


class AbstractUserVerify:
    """Common abstract class for user verification"""

    def _verify(self, user: AbstractUser) -> bool:
        """check user verification by condition"""
        raise NotImplementedError


class AbstractUserValidation(AbstractUserVerify, metaclass=ABCMeta):
    """Common abstract class for user validation"""

    exception: Type[VerificationError]

    def validate(self, user: AbstractUser):
        """Raise error if user has not passed verification"""
        raise NotImplementedError


class BaseUserValidation(AbstractUserValidation):
    exception = VerificationError
    message = 'ValidationError'

    def __init__(self, message=''):
        if message:
            self.message = message

    def _verify(self, user: AbstractUser) -> bool:
        raise NotImplementedError

    def validate(self, user):
        if not self._verify(user):
            raise self.exception(self.message)
