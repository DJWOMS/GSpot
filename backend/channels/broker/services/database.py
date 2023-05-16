from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoManager:
    client: AsyncIOMotorClient = None
    db: AsyncIOMotorDatabase = None

    async def connect(self, url):
        self.client = AsyncIOMotorClient(url, maxPoolSize=10, minPoolSize=10)
        self.session = await self.client.start_session()

    async def disconnect(self):
        self.client.close()
        self.session.end_session()

    async def ping_server(self):
        try:
            self.client.GSpot.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

<<<<<<< HEAD
    # async def do_insert(self, message):
    #     document = {'key': 'value'}
    #     result = await db.test_collection.insert_one(document)
=======

db = MongoManager()
>>>>>>> channels


db = MongoManager()