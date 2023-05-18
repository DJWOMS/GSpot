"""
Выполнение скрипта добавит все документы в коллекцию, выполняя план по порядку:
  # Создание пользователей
  # Вставка пользователей в базу данных
  # Создание уведомлений
  # Вставка уведомлений в базу данных
  # Создание комнаты
  # Вставка комнаты в базу данных
  # Создание участников комнаты
  # Вставка участников комнаты в базу данных
  # Создание сообщений
  # Вставка сообщений в базу данных
"""


from datetime import datetime
from pymongo import MongoClient

from chat.config.database import DatabaseConfig
# from models import User, Notification, Message, Room
from chat.src.messages.models import Message
from chat.src.notifications.models import Notification
from chat.src.rooms.models import Room
from chat.src.users.models import User, RoomParticipant

# Подключение к базе данных MongoDB
client = MongoClient("mongodb://localhost:27017")
# db = client["your_mongodb_db"]
# db: str = os.environ.get('MONGO_INITDB_DATABASE')
db = DatabaseConfig.db

# Создание пользователей
users = [
    User(username="user1", avatar="https://example.com/avatar1.png"),
    User(username="user2", avatar="https://example.com/avatar2.png")
]

# Вставка пользователей в базу данных
db["users"].insert_many([user.dict() for user in users])

# Создание уведомлений
notifications = [
    Notification(user_id=users[0].id, text="Notification 1", status="unread", created_at=datetime.utcnow()),
    Notification(user_id=users[1].id, text="Notification 2", status="unread", created_at=datetime.utcnow())
]

# Вставка уведомлений в базу данных
db["notifications"].insert_many([notification.dict() for notification in notifications])

# Создание комнаты
room = Room(room_name="Test Room", created_at=datetime.utcnow())

# Вставка комнаты в базу данных
db["rooms"].insert_one(room.dict())

# Создание участников комнаты
room_participants = [
    RoomParticipant(user_id=users[0].id, room_id=room.id),
    RoomParticipant(user_id=users[1].id, room_id=room.id)
]

# Вставка участников комнаты в базу данных
db["room_participants"].insert_many([participant.dict() for participant in room_participants])

# Создание сообщений
messages = [
    Message(sender_id=users[0].id, room_id="room_id", message_text="Message 1", created_at=datetime.utcnow()),
    Message(sender_id=users[1].id, room_id="room_id", message_text="Message 2", created_at=datetime.utcnow())
]

# Вставка сообщений в базу данных
db["messages"].insert_many([message.dict() for message in messages])
