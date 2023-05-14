from motor.motor_asyncio import AsyncIOMotorClient
from aio_pika.message import IncomingMessage
from ..abstract import RabbitMQConsumer
from aio_pika.queue import Queue


class NotificationConsumer(RabbitMQConsumer):
    queue_name = 'notifications'

    def __int__(self, queue: Queue, db_client: AsyncIOMotorClient):
        super().__init__(
            queue=queue,
            db_client=db_client,
        )

    async def process_message(self, orig_message: IncomingMessage):
        async with orig_message.process():
            await self.insert_message(orig_message.body)
            print(orig_message)
        # logger.info(orig_message.body)

    async def insert_message(self, message):
        print(message)
        db = self.db_client.GSpot
        collection = db.users
        document = {'key': 'value'}
        result = await collection.insert_one(document)
        print(result)
