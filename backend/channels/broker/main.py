import asyncio
from consumers.email.consumer import EmailConsumer
from consumers.notifications.consumer import NotificationConsumer
from services.rabbitmq import rabbit_connection
from services.database import db
from config.database import db_config
from config.rabbitmq import rabbitmq_config


async def main() -> None:
    await rabbit_connection.connect(rabbitmq_config.url)
    await db.connect(db_config.url)
    try:
        async with rabbit_connection.channel as channel:
            await channel.set_qos(prefetch_count=100)
            await db.ping_server()
            email_queue = await rabbit_connection.prepare_consumed_queue('email')
            notification_queue = await rabbit_connection.prepare_consumed_queue('notifications')
            email_consumer = EmailConsumer(queue=email_queue, db_client=db.client)
            notification_consumer = NotificationConsumer(queue=notification_queue, db_client=db.client)
            await rabbit_connection.publish('test', 'notifications')
            await rabbit_connection.publish('test', 'email')
            consuming_email, consuming_notifications = await asyncio.gather(email_consumer.consume(), notification_consumer.consume())

    finally:
        await rabbit_connection.disconnect()
        await db.disconnect()


if __name__ == "__main__":
    asyncio.run(main())
