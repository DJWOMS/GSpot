from abc import ABC, abstractmethod


class BaseTOTPToken(ABC):
    @staticmethod
    @abstractmethod
    def generate_totp() -> str:
        pass

    @staticmethod
    @abstractmethod
    def send_totp() -> str:
        pass

    @abstractmethod
    def send_to_channels(self, totp: str):
        pass

    @abstractmethod
    def add_to_redis(self, totp: str, data: dict):
        pass

    @abstractmethod
    def check_totp(self, totp: str):
        pass
