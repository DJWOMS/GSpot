import json
from dataclasses import dataclass
from typing import Any


@dataclass
class BaseMessage:
    exchange_name: str
    routing_key: str
    message: dict[str, Any]

    def to_bytes(self) -> bytes:
        message_json = json.dumps(self.message)
        return message_json.encode()


@dataclass
class DevActivationMessage(BaseMessage):
    exchange_name = 'dev_activation_exchange'
    routing_key = 'dev_activation_queue'


@dataclass
class ClientActivationMessage(BaseMessage):
    exchange_name = 'client_activation_exchange'
    routing_key = 'client_activation_queue'


@dataclass
class OwnerAccessMessage(BaseMessage):
    exchange_name = 'owner_access_exchange'
    routing_key = 'owner_access_queue'


@dataclass
class DevAccessMessage(BaseMessage):
    exchange_name = 'dev_access_exchange'
    routing_key = 'dev_access_queue'


@dataclass
class FriendAddedMessage(BaseMessage):
    exchange_name = 'friend_added_exchange'
    routing_key = 'friend_added_queue'
