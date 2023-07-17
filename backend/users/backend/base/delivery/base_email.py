from abc import ABC, abstractmethod

from utils.broker.message import (
    AdminActivationMessage,
    CustomerActivationMessage,
    DevelopActivationMessage,
)


class BaseEmail(ABC):
    @abstractmethod
    def send_email(
        self,
        message: AdminActivationMessage | CustomerActivationMessage | DevelopActivationMessage,
    ) -> str:
        pass
