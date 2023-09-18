from abc import ABC, abstractmethod

from base.models import BaseAbstractUser
from utils.broker.message import NotifyMessage


class BaseNotify(ABC):
    @abstractmethod
    def send_notify(
        self,
        message: NotifyMessage,
    ) -> str:
        pass
