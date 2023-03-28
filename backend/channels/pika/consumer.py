import asyncio
import aio_pika

RABBIT_URL = f'amqp://user:password@rabbitmq:5672/'


async def main() -> None:
    connection = await aio_pika.connect_robust(RABBIT_URL)

    queue_name = 'test_queue'

    async with connection:
        channel = await connection.channel()

        await channel.set_qos(prefetch_count=10)

        queue = await channel.declare_queue(queue_name, auto_delete=True)

        async with queue.iterator() as queue_iter:
            async for message in queue_iter:
                async with message.process():
                    print(message.body)

                    if queue.name in message.body.decode():
                        break


if __name__ == "__main__":
    asyncio.run(main())
