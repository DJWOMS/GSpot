from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase


class MongoManager:

    async def ping_server(self, client):
        try:
            client.GSpot.command('ping')
            print("Pinged your deployment. You successfully connected to MongoDB!")
        except Exception as e:
            print(e)

    # async def do_insert(self, message):
    #     document = {'key': 'value'}
    #     result = await db.test_collection.insert_one(document)


db = MongoManager()