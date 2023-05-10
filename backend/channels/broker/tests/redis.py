import asyncio
import unittest
from redis import Redis
from config.redis import redis_config
import redis.asyncio as redis
from redis.asyncio.client import PubSub
import os


class TestRedis(unittest.IsolatedAsyncioTestCase):

    def __init__(self, methodname):
        self._connect()
        super().__init__(methodname)

    def _connect(self):
        self.redis = redis.from_url(redis_config.url, encoding='utf-8', decode_responses=True)
        self.pubsub = self.redis.pubsub()

    async def test_connection(self):
        ping = await self.redis.ping()
        self.assertTrue(ping)

    async def test_pubsub(self):
        messages = ['hello', 'world']
        await self.pubsub.subscribe('channel1', 'channel2')
        future = asyncio.create_task(self.reader())
        await self.redis.publish('channel1', messages[0])
        await self.redis.publish('channel2', messages[1])
        await future

    async def reader(self):
        channels = ['channel1', 'channel2']
        messages = {'channel1': 'hello', 'channel2': 'world'}
        while True:
            message = await self.pubsub.get_message()
            if message is not None:
                if type(message['data']) is not int:
                    self.assertTrue(message['channel'] in channels)
                    self.assertEqual(message['data'], messages[message['channel']])
                    if message['channel'] == 'channel2':
                        break
