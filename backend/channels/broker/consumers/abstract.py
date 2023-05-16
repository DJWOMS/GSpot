import asyncio
from abc import ABCMeta, abstractmethod

from aio_pika.message import IncomingMessage


class RabbitMQConsumer(metaclass=ABCMeta):
    """RabbitMQ consumer abstract class responsible for consuming data from the queue."""

    def __init__(
        self,
        queue,
        iterator_timeout: int = 5,
        iterator_timeout_sleep: float = 5.0,
        *args,
        **kwargs,
    ):
        self.db_client = kwargs['db_client']
        self.queue = queue
        self.iterator_timeout = iterator_timeout
        self.iterator_timeout_sleep = iterator_timeout_sleep
        self.consuming_flag = True

    async def consume(self):
        """Consumes data from RabbitMQ queue forever until `stop_consuming()` is called."""
        async with self.queue.iterator(timeout=self.iterator_timeout) as queue_iterator:
            while self.consuming_flag:
                try:
                    async for orig_message in queue_iterator:
                        await self.process_message(orig_message)
                        if not self.consuming_flag:
                            break  # Breaks the queue iterator
                except asyncio.exceptions.TimeoutError:
                    await self.on_finish()
                    if self.consuming_flag:
                        await asyncio.sleep(self.iterator_timeout_sleep)
                finally:
                    await self.on_finish()

    @abstractmethod
    async def process_message(self, orig_message: IncomingMessage):
        raise NotImplementedError()

    def stop_consuming(self):
        """Stops the consuming gracefully"""
        self.consuming_flag = False

    async def on_finish(self):
        """Called after the message consuming finished."""
        pass