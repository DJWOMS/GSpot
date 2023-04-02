import json
from aio_pika.abc import AbstractIncomingMessage
from .email import sender


async def send_email(message: AbstractIncomingMessage) -> None:
    await sender.send_email(
        type_msg=message.routing_key,
        body=json.loads(message.body)
    )
