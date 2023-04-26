from abc import ABCMeta
from typing import Type

from django.contrib.auth.models import AbstractUser


class AbstractUserVerification(metaclass=ABCMeta):
    """ Common abstract class for user verification """

    def verify(self, user: AbstractUser):
        pass


class VerificationError(Exception):
    """ Common base class for all verification exceptions. """
    message = 'user verification error'

    def __init__(self, *args, **kwargs):
        super().__init__(self.message, *args)


class BaseUserVerification(AbstractUserVerification):
    exception: Type[VerificationError]

    def _condition(self, user) -> bool:
        raise NotImplementedError

    def verify(self, user):
        if self._condition(user):
            raise self.exception()
