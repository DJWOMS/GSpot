from abc import ABCMeta
from typing import Union, Type

from django.utils.translation import gettext_lazy as _

from administrator.models import Admin
from customer.models import CustomerUser
from developer.models import CompanyUser


class AbstractUserVerification(metaclass=ABCMeta):
    """ Common abstract class for user verification """

    def verify(self, user: Union[CustomerUser, Admin, CompanyUser]):
        pass


class VerificationError(Exception):
    """ Common base class for all verification exceptions. """


class BaseUserVerification(AbstractUserVerification):
    exception: Type[VerificationError]
    message: str

    def _condition(self, user: Union[CustomerUser, Admin, CompanyUser]):
        raise NotImplementedError

    def verify(self, user):
        if self._condition(user):
            raise self.exception(_(self.message))
