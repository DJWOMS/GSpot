from typing import Type
from fastapi import APIRouter, Depends
from gspot_fastapi_auth import BaseUser, UserRedisAuth

from ..repository import NotificationRepo
from ..schema import NotificationResponse

notification = APIRouter(prefix='/notification')


@notification.get('/user/')
async def get_user_notification(user: Type[BaseUser] = Depends(UserRedisAuth())):
    notifications = await NotificationRepo.get_user_notification(str(user.user_id))
    return NotificationResponse(
        code='200',
        status='ok',
        message='Success retrieve user\'s notifications',
        result=notifications,
    )
