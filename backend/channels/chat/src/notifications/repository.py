from .models import Notification
from core.database import db


class NotificationRepo:

    @staticmethod
    async def create(notification: Notification):
        await db.client.your_mongodb_db.get_collection('notification').insert_one(notification.dict())

    @staticmethod
    async def get_by_id(_id: str):
        return await db.client.your_mongodb_db.get_collection('notification').find_one({'_id': _id})

    @staticmethod
    async def get_user_notification(user_id: str):
        _notifications = []
        collection = db.client.your_mongodb_db.get_collection('notification').find({'user_id': user_id})
        async for notification in collection:
            _notifications.append(notification)
        return _notifications

    @staticmethod
    async def update_status_notification(_id: str, status: str):
        await db.client.your_mongodb_db.get_collection('notification').update_one({'_id': _id}, {'$set': {'status': status}})
        return NotificationRepo.get_by_id(_id)
