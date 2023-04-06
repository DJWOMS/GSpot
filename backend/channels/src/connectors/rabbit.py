import json
import logging
from dataclasses import dataclass
from aio_pika import connect_robust, Message
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel
from config import RABBIT_URL, settings


@dataclass
class RabbitConnection:
    connection: AbstractRobustConnection | None = None
    channel: AbstractRobustChannel | None = None

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

    async def connect(self) -> None:
        try:
            self.connection = await connect_robust(RABBIT_URL)
            self.channel = await self.connection.channel(publisher_confirms=False)
        except Exception as e:
            await self._clear()
            logging.error(e.__dict__)

    async def disconnect(self) -> None:
        await self._clear()

    async def send_messages(
            self,
            messages: list | dict,
            routing_key: str = settings.RABBITMQ_TEST_QUEUE
    ) -> None:
        if not self.channel:
            raise RuntimeError('RabbitMQ connection not establish')

        if isinstance(messages, dict):
            messages = [messages]

        async with self.channel.transaction():
            for message in messages:
                message = Message(
                    body=json.dumps(message).encode()
                )

                await self.channel.default_exchange.publish(
                    message, routing_key=routing_key,
                )


rabbit_connection = RabbitConnection()
