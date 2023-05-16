from motor.motor_asyncio import AsyncIOMotorClient
from aio_pika.message import IncomingMessage
from ..abstract import RabbitMQConsumer
from aio_pika.queue import Queue
import logging


logger = logging.getLogger(__name__)


class EmailConsumer(RabbitMQConsumer):
    queue_name = 'email'

    def __int__(self, queue: Queue, db_client: AsyncIOMotorClient, *args, **kwargs):
        super().__init__(
            queue=queue,
            db_client=db_client
        )

    async def process_message(self, orig_message: IncomingMessage):
        async with orig_message.process():
            print('сообщение отработано и успешно удалено из очереди в консьюмере mail')
        # await self.db_client.do_insert(orig_message)
        logger.info(orig_message.body)

