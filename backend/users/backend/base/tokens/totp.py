from abc import ABC, abstractmethod

from base.models import BaseAbstractUser


class BaseTOTPToken(ABC):
    @staticmethod
    @abstractmethod
    def generate_totp() -> str:
        pass

    @staticmethod
    @abstractmethod
    def send_totp(user: BaseAbstractUser) -> str:
        pass

    @abstractmethod
    def send_to_channels(self, totp: str, user: BaseAbstractUser):
        pass

    @abstractmethod
    def add_to_redis(self, totp: str, user: BaseAbstractUser):
        pass

    @abstractmethod
    def check_totp(self, totp: str):
        pass
