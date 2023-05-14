import unittest
import asyncio
import aio_pika
from config.rabbitmq import rabbitmq_config


class TestRabbitmq(unittest.IsolatedAsyncioTestCase):

    async def _connect(self):
        self.rabbitmq_connection = await aio_pika.connect_robust(rabbitmq_config.url, loop=asyncio.get_event_loop())
        self.rabbitmq_channel = await self.rabbitmq_connection.channel(publisher_confirms=False)

    async def _disconnect(self):
        await self.rabbitmq_connection.close()

    async def test_email_consumer(self):
        await self._connect()

