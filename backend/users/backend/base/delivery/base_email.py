from abc import ABC, abstractmethod

from utils.broker.message import BaseMessage


class BaseEmail(ABC):
    @abstractmethod
    def send_email(
        self,
        message: BaseMessage,
    ) -> str:
        pass
