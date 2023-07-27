from typing import Any, Dict, List

from core.database import db


async def get_room_messages(room_id: str) -> List[Dict[str, Any] | None]:
    messages = []
    collection = db.client.your_mongodb_db.get_collection('messages').find({'room_id': room_id})
    async for message in collection:
        messages.append(message)
    return messages


async def get_room_participant(room_id: str, user_id: str) -> List[Dict[str, Any] | None]:
    user = (
        await db.client.your_mongodb_db.get_collection('room_participant').find_one({
            'room_id': room_id, 'user_id': user_id})
    )
    return user
