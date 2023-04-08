from .email import sender


async def send_email(message: dict) -> None:
    await sender.send_email(
        type_msg='test_queue',
        body=message
    )
