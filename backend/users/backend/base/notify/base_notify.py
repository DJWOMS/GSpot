from abc import ABC, abstractmethod

from base.models import BaseAbstractUser
from utils.broker.message import NotifyMessage


class BaseNotify(ABC):
    @abstractmethod
    def send_notify(
        self,
        user: BaseAbstractUser,
        sender_user: BaseAbstractUser,
        message: NotifyMessage,
    ) -> str:
        pass
