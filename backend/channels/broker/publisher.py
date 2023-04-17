import aio_pika
from aio_pika.pool import Pool
from services.rabbitmq import RabbitManager


async def publish(rabbitmq: RabbitManager):
    print('asdas')
    # await channel.default_exchange.publish(
    #         aio_pika.Message(("Channel: GSpot" % channel).encode()),
    #         'email',
    # )