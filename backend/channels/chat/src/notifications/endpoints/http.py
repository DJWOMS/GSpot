from fastapi import APIRouter

from ..repository import NotificationRepo
from ..schema import NotificationResponse

notification = APIRouter(prefix='/notification')


@notification.get('/user/')
async def get_user_notification(user):  # TODO middle ware return user by token
    notifications = await NotificationRepo.get_user_notification(user)
    return NotificationResponse(
        code='200',
        status='ok',
        message='Success retrieve user\'s notifications',
        result=notifications,
    )
