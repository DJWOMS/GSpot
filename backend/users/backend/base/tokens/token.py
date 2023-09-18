from abc import ABC, abstractmethod


class BaseToken(ABC):
    @abstractmethod
    def generate_access_token(self, data: dict):
        pass

    @abstractmethod
    def generate_refresh_token(self, data: dict):
        pass

    @abstractmethod
    def check_token(self, token: str):
        pass
