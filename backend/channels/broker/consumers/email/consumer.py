import json
import logging
from email.message import EmailMessage

import aiosmtplib
from aio_pika.message import IncomingMessage
from aio_pika.queue import Queue
from config.database import db_config
from config.smtp import smtp_config
from motor.motor_asyncio import AsyncIOMotorClient
from pydantic.error_wrappers import ValidationError

from ..abstract import RabbitMQConsumer
from .models import Mail

logger = logging.getLogger(__name__)


class EmailConsumer(RabbitMQConsumer):
    queue_name = 'email'

    def __init__(self, queue: Queue, db_client: AsyncIOMotorClient):
        super().__init__(
            queue=queue,
            db_client=db_client
        )
        self.db = db_client[db_config.db]

    async def process_message(self, orig_message: IncomingMessage):
        async with orig_message.process():
            try:
                msg = json.loads(orig_message.body)
                mail = Mail(**msg)

                smtp_client = aiosmtplib.SMTP(
                    hostname=smtp_config.SMTP_HOST,
                    port=smtp_config.SMTP_PORT,
                    use_tls=True
                )

                message = EmailMessage()
                message['Subject'] = mail.subject
                message['From'] = smtp_config.EMAIL_ADDRESS
                message['To'] = mail.email
                message.set_content(mail.body, subtype='html')

                async with smtp_client:
                    await smtp_client.login(username=smtp_config.EMAIL_ADDRESS, password=smtp_config.EMAIL_PASSWORD)
                    await smtp_client.send_message(message)

                self.db.email.insert_one(msg)

                logger.info(f'Сообщение отправлено {msg}')

            except (ValidationError, json.JSONDecodeError, aiosmtplib.SMTPDataError):
                logger.error(f'Не удалось отправить сообщение {orig_message.body}')
