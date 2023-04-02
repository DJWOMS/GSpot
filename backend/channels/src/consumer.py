import asyncio
import json
import aio_pika
from config import RABBIT_URL, settings
from pika.tasks import send_email
from schemas.pika import AioMessage


async def process_message(
        message: aio_pika.abc.AbstractIncomingMessage,
) -> None:
    async with message.process():
        body = json.loads(message.body.decode())
        message = AioMessage.parse_obj(body)
        if message.type == 'email':
            await send_email(body)
            return
        elif message.type == 'notification':
            # Save notifications task here
            return
        else:
            # Print test message
            print(body)


async def main() -> None:
    connection = await aio_pika.connect_robust(RABBIT_URL)

    queue_name = settings.RABBITMQ_TEST_QUEUE

    async with connection:
        channel = await connection.channel()
        await channel.set_qos(prefetch_count=10)  # Max number of parallel tasks
        queue = await channel.declare_queue(queue_name, auto_delete=True)

        await queue.consume(process_message)  # Callback for perform message if received

        try:
            await asyncio.Future()  # Wait until terminate worker
        finally:
            await connection.close()


if __name__ == "__main__":
    asyncio.run(main())
