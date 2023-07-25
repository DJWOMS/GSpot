import json
import logging

from aio_pika.message import IncomingMessage
from aio_pika.queue import Queue
from bson import ObjectId
from motor.motor_asyncio import AsyncIOMotorClient

from ..abstract import RabbitMQConsumer
from .models import Notification

logger = logging.getLogger(__name__)

class NotificationConsumer(RabbitMQConsumer):
    queue_name = 'notifications'

    def __int__(self, queue: Queue, db_client: AsyncIOMotorClient):
        super().__init__(
            queue=queue,
            db_client=db_client,
        )

    async def process_message(self, orig_message: IncomingMessage):
        async with orig_message.process():
            message_data = json.loads(orig_message.body)
            message_data['user_id'] = ObjectId(message_data['user_id'])
            notification_data = Notification(**message_data)

            await self.db_client.your_mongodb_db.get_collection('notification').insert_one(notification_data.dict())

        logger.info(orig_message.body)
