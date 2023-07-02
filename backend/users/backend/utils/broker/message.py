import json
from dataclasses import dataclass
from typing import Any

from django.conf import settings


@dataclass
class BaseMessage:
    message: dict[str, Any]
    exchange_name: str
    routing_key: str

    def to_bytes(self) -> bytes:
        message_json = json.dumps(self.message)
        return message_json.encode()


@dataclass
class DevActivationMessage(BaseMessage):
    exchange_name: str = "dev_activation_exchange"
    routing_key: str = "dev_activation_queue"


@dataclass
class ClientActivationMessage(BaseMessage):
    exchange_name: str = "client_activation_exchange"
    routing_key: str = "client_activation_queue"


@dataclass
class OwnerAccessMessage(BaseMessage):
    exchange_name: str = "owner_access_exchange"
    routing_key: str = "owner_access_queue"


@dataclass
class DevAccessMessage(BaseMessage):
    exchange_name: str = "dev_access_exchange"
    routing_key: str = "dev_access_queue"


@dataclass
class FriendAddedMessage(BaseMessage):
    exchange_name: str = "friend_added_exchange"
    routing_key: str = "friend_added_queue"


@dataclass
class TOTPTokenMessage(BaseMessage):
    exchange_name: str = settings.TOTP_EXCHANGE_NAME
    routing_key: str = settings.TOTP_ROUTING_KEY
