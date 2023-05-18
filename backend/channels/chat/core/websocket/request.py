import json
from typing import Literal
from pydantic import BaseModel, validator, ValidationError

from src.notifications.models import Notification
from src.messages.models import Message


class WebsocketRequest(BaseModel):
    user_id: str
    action: Literal['create', 'update']
    # type: Literal['message', 'notification']
    path: str
    body: dict

    @validator('body', pre=True)
    def prepare_body(cls, v):
        if isinstance(v, str):
            try:
                return json.loads(v).decode('utf-8')
            except json.JSONDecodeError:
                raise ValueError('Invalid body value. Should be JSON-object')
        return v

    @validator('action')
    def action_validator(cls, v):
        if v not in ['create', 'update']:
            raise ValueError('Action must be `create` or `update`')
        return v

    # @validator('type')
    # def type_validator(cls, v):
    #     if v not in ['message', 'notification']:
    #         raise ValueError('Type must be `message` or `notification`')
    #     return v

    @validator('body')
    def body_validator(cls, v, values):
        if not isinstance(v, dict):
            raise ValueError('Body should be `dict` object')
        # class_validator = Message if values.get('type') == 'message' else Notification
        print(v, values)
        # try:
        #     class_validator.parse_obj(v)
        # except ValidationError:
        #     raise ValueError('Invalid body content')
        return v

    class Config:
        schema_extra = {
            'example': {
                'action': 'update',
                'path': 'message',
                'body': {
                    "sender_id": "6148ed23aa02a1a38bde5e5d",
                    "room_id": "6148ed23aa02a1a38bde5e5c",
                    "message_text": "Hello, world!",
                    "created_at": "2023-04-22T12:00:00.000Z"
                }
            }
        }