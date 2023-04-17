import os
from aio_pika.channel import Channel
from aio_pika.queue import Queue


DEFAULT_QUEUE_PARAMETERS = {
    "durable": True,
    "arguments": {
        "x-queue-type": "classic",
    },
}


async def _prepare_consumed_queue(channel: Channel, queue) -> Queue:
    if os.environ.get('DEAD_LETTER_QUEUE_NAME'):
        DEFAULT_QUEUE_PARAMETERS["arguments"]["x-queue-type"] = 'classic'
    queue = await channel.declare_queue(
        queue,
        **DEFAULT_QUEUE_PARAMETERS,
    )
    await queue.bind(os.environ.get('EXCHANGE'))
    return queue

