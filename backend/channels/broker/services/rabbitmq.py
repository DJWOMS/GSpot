import aio_pika
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel
from aio_pika.queue import Queue
import os


class RabbitManager:
    connection: AbstractRobustConnection | None = None
    channel: AbstractRobustChannel | None = None
    DEFAULT_QUEUE_PARAMETERS = {
        "durable": True,
        "arguments": {
            "x-queue-type": "classic",
        },
    }

    def status(self) -> bool:
        if self.connection.is_closed or self.channel.is_closed:
            return False
        return True

    async def _clear(self) -> None:
        if self.channel and not self.channel.is_closed:
            await self.channel.close()
        if self.connection and not self.connection.is_closed:
            await self.connection.close()
        self.connection = None
        self.channel = None

    async def connect(self, url) -> None:
        try:
            self.connection = await aio_pika.connect_robust(url)
            self.channel = await self.connection.channel(publisher_confirms=False)
        except Exception as e:
            print(e)
            await self._clear()

    async def disconnect(self) -> None:
        await self._clear()

    async def publish(self, message: str, routing_key):
        exchange = await self.channel.declare_exchange('GSpot', durable=True)
        ready_queue = await self.channel.declare_queue(routing_key, durable=True)
        await ready_queue.bind(exchange, routing_key)
        await exchange.publish(
            aio_pika.Message(
                body=message.encode(),
                delivery_mode=aio_pika.DeliveryMode.PERSISTENT
            ),
            routing_key
        )

    async def prepare_consumed_queue(self, channel, queue) -> Queue:
        # if os.environ.get('DEAD_LETTER_QUEUE_NAME'):
        #     DEFAULT_QUEUE_PARAMETERS["arguments"]["x-queue-type"] = 'classic'
        queue = await channel.declare_queue(
            queue,
            **self.DEFAULT_QUEUE_PARAMETERS,
        )
        await queue.bind(os.environ.get('EXCHANGE'))
        return queue


rabbit_connection = RabbitManager()
