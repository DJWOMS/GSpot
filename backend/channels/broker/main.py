import asyncio
import logging
from consumers.email.consumer import EmailConsumer
from consumers.notifications.consumer import NotificationConsumer
from core.utills import ChannelsContextManager


async def main() -> None:
    try:
        async with ChannelsContextManager() as manager:
            email_queue = await manager.prepare_consumed_queue('email')
            notifications_queue = await manager.prepare_consumed_queue('notifications')
            email_consumer = EmailConsumer(queue=email_queue, db_client=manager.db_client)
            notification_consumer = NotificationConsumer(queue=notifications_queue, db_client=manager.db_client)
            email, notif = await asyncio.gather(email_consumer.consume(), notification_consumer.consume())
    except ConnectionError:
        logging.warning('databus service is not running, please start databus service and restart this service')


if __name__ == "__main__":
    asyncio.run(main())
