import json

from aio_pika.abc import AbstractIncomingMessage

from channels.notifications.sender_email import sender


async def send_email(message: AbstractIncomingMessage) -> None:
    async with message.process():
        sender.send_email(
            type_msg=message.routing_key,
            body=json.loads(message.body)
        )
