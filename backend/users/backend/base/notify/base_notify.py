from abc import ABC, abstractmethod

from base.models import BaseAbstractUser


class BaseNotify(ABC):
    @abstractmethod
    def send_notify(self, user: BaseAbstractUser, sender_user: BaseAbstractUser) -> str:
        pass

    @abstractmethod
    def send_to_channels(self, user: BaseAbstractUser, sender_user: BaseAbstractUser):
        pass
