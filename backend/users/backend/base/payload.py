from abc import ABC, abstractmethod


class BasePayload(ABC):
    @abstractmethod
    def generate_payload(self) -> dict:
        pass
