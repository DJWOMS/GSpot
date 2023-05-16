from typing import Optional

from motor.motor_asyncio import (
    AsyncIOMotorClient,
    AsyncIOMotorCollection,
    AsyncIOMotorDatabase,
)


class MongoManager:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect(self, url: str):
        self.client = AsyncIOMotorClient(url, maxPoolSize=10, minPoolSize=10)
        self.db = self.client.get_default_database()

    async def disconnect(self):
        self.client.close()

    async def ping_server(self):
        try:
            self.client.admin.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    def set_db(self, db: AsyncIOMotorDatabase):
        self.db = db

    async def get_collection(self, name: str) -> Optional[AsyncIOMotorCollection]:
        return self.db[name] if self.db is not None else None

    async def insert_one(self, collection_name: str, document: dict):
        collection = await self.get_collection(collection_name)
        if collection is not None:
            await collection.insert_one(document)

    async def find_one(self, collection_name: str, filter: dict) -> Optional[dict]:
        collection = await self.get_collection(collection_name)
        return await collection.find_one(filter) if collection is not None else None

    async def find_many(self, collection_name: str, filter: dict) -> list:
        collection = await self.get_collection(collection_name)
        cursor = collection.find(filter)
        return [document async for document in cursor]

    async def update_one(self,
                         collection_name: str,
                         filter: dict,
                         update: dict,
                         upsert: bool = False) -> None:
        collection = await self.get_collection(collection_name)
        await collection.update_one(filter, {'$set': update}, upsert=upsert)

    async def update_many(self,
                          collection_name: str,
                          filter: dict,
                          update: dict,
                          upsert: bool = False) -> None:
        collection = await self.get_collection(collection_name)
        await collection.update_many(filter, {'$set': update}, upsert=upsert)

    async def delete_one(self, collection_name: str, filter: dict) -> None:
        collection = await self.get_collection(collection_name)
        await collection.delete_one(filter)

    async def delete_many(self, collection_name: str, filter: dict) -> None:
        collection = await self.get_collection(collection_name)
        await collection.delete_many(filter)


db = MongoManager()
