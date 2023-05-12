import asyncio
import logging

from fastapi import WebSocketDisconnect
from pydantic import ValidationError
from redis.exceptions import ConnectionError, PubSubError

from .models import ClientAction
from .utils import ConnectionContextManager


async def consumer_handler(service: ConnectionContextManager):
    try:
        while True:
            await asyncio.sleep(0.1)
            received_data = await service.websocket.receive_json()
            try:
                data = ClientAction.parse_obj(received_data["message"])
                await service.ws_controller.rout(collection=data.type, action=data.action, data=data)
                logging.debug(data)
            except ValidationError as e:
                await service.websocket.send_json({"error": e.errors()[0]['msg']})
    except WebSocketDisconnect:
        logging.debug("WebSocketDisconnect - consumer handler disconnected")


async def producer_handler(service: ConnectionContextManager):
    try:
        async with service.pubsub as pubsub:
            while True:
                if pubsub.subscribed:
                    message = await pubsub.get_message(ignore_subscribe_messages=True, timeout=None)
                    if message:
                        await service.websocket.send_json(message['data'].decode())
    except (ConnectionError, PubSubError) as e:
        logging.debug(f"{e.__class__}", "producer handler disconnected", exc_info=e)
