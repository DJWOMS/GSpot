from typing import Literal

from pydantic import BaseModel


class AioMessage(BaseModel):
    type: Literal['email', 'notification', 'test']
