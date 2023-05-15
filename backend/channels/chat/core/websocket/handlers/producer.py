from fastapi import WebSocket
from core.websocket.request import WebsocketRequest
from pydantic.error_wrappers import ValidationError


class ProducerHandler:
    websocket: WebSocket

    def __init__(self, websocket: WebSocket):
        self.websocket = websocket

    async def handle_event(self, data):
        try:
            WebsocketRequest.parse_obj(data)
        except ValidationError as e:
            errors = {f'{x["loc"]}': f'{x["msg"]}' for x in e.errors()}
            await self.websocket.send_json(errors)

