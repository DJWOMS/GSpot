import asyncio
import aio_pika
import os
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel
from aio_pika.queue import Queue


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
