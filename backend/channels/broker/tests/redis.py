import asyncio
import unittest
from redis import Redis
from config.redis import redis_config
import redis.asyncio as redis
from redis.asyncio.client import PubSub


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
        await self.redis.publish('channel1', messages[0])
        await self.redis.publish('channel2', messages[1])
        await self.reader()
        await self.pubsub.close()

    async def reader(self):
        result = {
            'channel1': 'hello',
            'channel2': 'world'
        }
        messages = {}
        while True:
            message = await self.pubsub.get_message()
            if message is not None:
                if type(message['data']) is not int:
                    messages[message['channel']] = message['data']
                    if message['channel'] == 'channel2':
                        self.assertDictEqual(messages, result)
                        break