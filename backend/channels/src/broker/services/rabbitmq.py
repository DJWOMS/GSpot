import aio_pika
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel
from dataclasses import dataclass


@dataclass
class RabbitManager:
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

    async def connect(self, url) -> None:
        try:
            self.connection = await aio_pika.connect_robust(url)
            self.channel = await self.connection.channel(publisher_confirms=False)
        except Exception as e:
            print(e)
            await self._clear()

    async def disconnect(self) -> None:
        await self._clear()


rabbit_connection = RabbitManager()
