from typing import Optional

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)


class MongoManager:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect(self, url):
        self.client = AsyncIOMotorClient(url, maxPoolSize=10, minPoolSize=10)
        self.db = self.client.get_default_database()

    async def disconnect(self):
        self.client.close()

    async def ping_server(self):
        # Replace the placeholder with your Atlas connection string
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def set_db(self, db: AsyncIOMotorDatabase):
        self.db = db

    async def get_collection(self, name: str) -> Optional[AsyncIOMotorCollection]:
        return self.db[name] if self.db else None

    async def insert_one(self, collection_name: str, document: dict):
        collection = self.get_collection(collection_name)
        if collection:
            await collection.insert_one(document)

    async def find_one(self, collection_name: str, filter: dict) -> Optional[dict]:
        collection = self.get_collection(collection_name)
        return await collection.find_one(filter) if collection else None


db = MongoManager()
