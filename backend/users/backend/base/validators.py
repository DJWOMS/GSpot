from abc import ABCMeta
from typing import Type

from django.contrib.auth.models import AbstractUser


class AbstractUserVerify(metaclass=ABCMeta):
    """Common abstract class for user verification """

    def verify(self, user: AbstractUser) -> bool:
        """ check user verification by condition """
        pass


class VerificationError(Exception):
    """ Common base class for all verification exceptions. """
    message = 'user verification error'

    def __init__(self, *args, **kwargs):
        super().__init__(self.message, *args)


class AbstractUserValidation(AbstractUserVerify, metaclass=ABCMeta):
    """ Common abstract class for user validation """
    exception: Type[VerificationError]

    def validate(self, user: AbstractUser):
        """Raise error if user has not passed verification """
        pass


class BaseUserValidation(AbstractUserValidation):

    def validate(self, user):
        if not self.verify(user):
            raise self.exception()
