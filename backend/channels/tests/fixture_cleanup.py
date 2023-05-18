"""
Выполнение скрипта удалит все документы из коллекций:
    users,
    notifications,
    messages,
    rooms,
    room_participants
- очищая базу данных (DatabaseConfig.db).
"""

from pymongo import MongoClient

from chat.config.database import DatabaseConfig

# Подключение к базе данных MongoDB
client = MongoClient("mongodb://localhost:27017")
# db = client["your_database_name"]
db = DatabaseConfig.db

# Удаление всех документов из коллекций
db["users"].delete_many({})
db["notifications"].delete_many({})
db["messages"].delete_many({})
db["rooms"].delete_many({})
db["room_participants"].delete_many({})

print("fixture_cleanup | Cleanup completed.")
