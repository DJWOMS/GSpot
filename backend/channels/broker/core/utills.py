import redis.asyncio as redis
from redis.asyncio.client import PubSub, Redis
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from aio_pika.abc import AbstractRobustConnection, AbstractRobustChannel
import aio_pika
import asyncio

from config.redis import redis_config
from config.database import db_config
from config.rabbitmq import rabbitmq_config

from services.database import MongoManager
from services.rabbitmq import RabbitManager


class ChannelsContextManager(MongoManager, RabbitManager):
    rabbitmq_connection: AbstractRobustConnection
    rabbitmq_channel: AbstractRobustChannel
    pubsub: PubSub
    redis: Redis = redis.from_url(
        redis_config.url,
        encoding='utf-8',
        decode_responses=True
    )
    db_client: AsyncIOMotorClient = AsyncIOMotorClient(db_config.url, maxPoolSize=10, minPoolSize=10)
    db_session: AsyncIOMotorDatabase

    def __init__(self):
        self.pubsub = self.redis.pubsub()

    async def _connect(self):
        self.rabbitmq_connection = await aio_pika.connect_robust(rabbitmq_config.url, loop=asyncio.get_event_loop())
        self.rabbitmq_channel = await self.rabbitmq_connection.channel(publisher_confirms=False)
        self.db_session = await self.db_client.start_session()

    async def _disconnect(self):
        await self.pubsub.close()
        await self.rabbitmq_connection.close()
        self.db_client.close()
        self.db_session.end_session()

    async def __aenter__(self):
        await self._connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb) -> None:
        await self._disconnect()

    async def prepare_consumed_queue(self, queue: str):
        queue = await super(ChannelsContextManager, self).prepare_consumed_queue(self.rabbitmq_channel, queue)
        return queue