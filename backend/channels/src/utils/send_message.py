import json
import aio_pika
from aio_pika.abc import AbstractRobustChannel

from config import settings


async def send_messages(
        channel: AbstractRobustChannel,
        messages: list | dict
):
    if isinstance(messages, dict):
        messages = [messages]

    async with channel.transaction():
        for message in messages:
            message = aio_pika.Message(body=json.dumps(message).encode())

            await channel.default_exchange.publish(
                message, routing_key=settings.RABBITMQ_TEST_QUEUE,
            )
