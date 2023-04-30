import aio_pika
from aio_pika.channel import Channel


async def publish(channel: Channel):
    await channel.default_exchange.publish(
            aio_pika.Message(("Channel: ыфвфывф" % channel).encode()),
            'email',
    )
