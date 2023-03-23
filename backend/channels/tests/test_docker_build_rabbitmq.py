import pytest
import os
import aio_pika


@pytest.mark.usefixtures("pika_test_connection")
def test_rabbitmq_connection(pika_test_connection):
    test_queue, test_body = str(os.environ.get("RABBITMQ_TEST_QUEUE")), "Body rabbitmq"

    with pika_test_connection.channel() as channel:
        channel.queue_declare(queue=test_queue)
        channel.basic_publish(exchange='', routing_key=test_queue, body=test_body)

        def callback(_ch, _method, _properties, body):
            assert body.decode() == test_body
            raise KeyboardInterrupt

        try:
            channel.basic_consume(queue=test_queue, on_message_callback=callback)
            channel.start_consuming()
        except KeyboardInterrupt:
            pass

        channel.queue_delete(queue=test_queue)


@pytest.mark.usefixtures("aio_pika_test_connection")
async def test_async_rabbitmq_connection(aio_pika_test_connection):
    test_queue, test_body = str(os.environ.get("RABBITMQ_TEST_QUEUE")), "Body async rabbitmq"
    read_message: bytes

    async with aio_pika_test_connection:
        channel = await aio_pika_test_connection.channel()
        await channel.set_qos(prefetch_count=1)
        queue = await channel.declare_queue(test_queue, auto_delete=True)
        async with queue.iterator() as queue_iter:
            await channel.default_exchange.publish(
                aio_pika.Message(body=test_body.encode()),
                routing_key=test_queue,
            )
            async for message in queue_iter:
                async with message.process():
                    read_message = message.body
                    break

    assert read_message.decode() == test_body
