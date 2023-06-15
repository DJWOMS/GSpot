import json
from dataclasses import dataclass
from typing import Any


@dataclass(init=False)
class BaseMessage:
    exchange_name: str
    routing_key: str
    message: dict[str, Any]

    def to_bytes(self) -> bytes:
        message_json = json.dumps(self.message)
        return message_json.encode()


@dataclass(init=False)
class DevActivationMessage(BaseMessage):
    exchange_name = 'dev_activation_exchange'
    routing_key = 'dev_activation_queue'


@dataclass(init=False)
class ClientActivationMessage(BaseMessage):
    exchange_name = 'client_activation_exchange'
    routing_key = 'client_activation_queue'


@dataclass(init=False)
class OwnerAccessMessage(BaseMessage):
    exchange_name = 'owner_access_exchange'
    routing_key = 'owner_access_queue'


@dataclass(init=False)
class DevAccessMessage(BaseMessage):
    exchange_name = 'dev_access_exchange'
    routing_key = 'dev_access_queue'


@dataclass(init=False)
class FriendAddedMessage(BaseMessage):
    exchange_name = 'friend_added_exchange'
    routing_key = 'friend_added_queue'


@dataclass(init=False)
class DevTOTPTokenMessage(BaseMessage):
    exchange_name = 'dev_totp_exchange'
    routing_key = 'dev_totp_queue'
