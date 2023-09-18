from fastapi import WebSocket
import sys
from core.websocket.request import WebsocketRequest
from pydantic.error_wrappers import ValidationError


class ProducerHandler:

    async def handle_event(self, data):
        sys.path.insert(0, '.')
        from main import chat
        try:
            request = WebsocketRequest.parse_obj(data)
            await chat.handle(request)
        except ValidationError as e:
            errors = {f'{x["loc"]}': f'{x["msg"]}' for x in e.errors()}
            await self.websocket.send_json(errors)
