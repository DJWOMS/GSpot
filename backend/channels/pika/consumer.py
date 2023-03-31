import asyncio
import json
import aio_pika
from .settings import settings
from typing import Literal
from pydantic import BaseModel

RABBIT_URL = f'amqp://{settings.RABBITMQ_DEFAULT_USER}:{settings.RABBITMQ_DEFAULT_PASS}' \
             f'@{settings.RABBITMQ_LOCAL_HOST_NAME}:{settings.RABBITMQ_LOCAL_PORT}/'


class AioMessage(BaseModel):
    type: Literal['email', 'notification']


async def process_message(
        message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    async with message.process():
        body = json.loads(message.body)
        message = AioMessage.parse_obj(body)
        if message.type == 'email':
            # Email task here
            return
        else:
            # Save notifications task here
            return


async def main() -> None:
    connection = await aio_pika.connect_robust(RABBIT_URL)

    queue_name = settings.RABBITMQ_TEST_QUEUE

    async with connection:
        channel = await connection.channel()

        await channel.set_qos(prefetch_count=10)

        queue = await channel.declare_queue(queue_name, auto_delete=True)

        await queue.consume(process_message)

        try:
            await asyncio.Future()
        finally:
            await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
