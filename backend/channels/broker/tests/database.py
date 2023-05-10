import unittest
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase, AsyncIOMotorCollection
from config.database import db_config
from bson.binary import JAVA_LEGACY
from bson import CodecOptions
from pymongo import ReadPreference, WriteConcern
from pymongo.read_preferences import Secondary


class TestDatabase(unittest.IsolatedAsyncioTestCase):

    def __init__(self, methodname):
        self.db = db_config.db
        self._connect()
        super().__init__(methodname)

    def _connect(self):
        self.db_client = AsyncIOMotorClient(db_config.url, maxPoolSize=10, minPoolSize=10)
        self.db_session = AsyncIOMotorDatabase(self.db_client, self.db)

    def test_database(self):
        self.assertEqual(self.db_session.name, self.db)

    async def test_create_collection(self):
        db = self.db_session
        collection = await db.create_collection('test_collection')
        self.assertTrue(isinstance(collection, AsyncIOMotorCollection))
        db.drop_collection('test_collection')

    async def test_drop_collection(self):
        db = self.db_session
        collection = db.test_drop_collection
        await collection.insert_one({})
        names = await db.list_collection_names()
        self.assertTrue("test_drop_collection" in names)
        await db.drop_collection(collection)
        names = await db.list_collection_names()
        self.assertFalse("test_drop_collection" in names)

    def test_get_collection(self):
        codec_options = CodecOptions(tz_aware=True, uuid_representation=JAVA_LEGACY)
        write_concern = WriteConcern(w=2, j=True)
        coll = self.db_session.get_collection("foo", codec_options, ReadPreference.SECONDARY, write_concern)

        self.assertTrue(isinstance(coll, AsyncIOMotorCollection))
        self.assertEqual("foo", coll.name)
        self.assertEqual(codec_options, coll.codec_options)
        self.assertEqual(ReadPreference.SECONDARY, coll.read_preference)
        self.assertEqual(write_concern, coll.write_concern)

        pref = Secondary([{"dc": "sf"}])
        coll = self.db_session.get_collection("foo", read_preference=pref)
        self.assertEqual(pref, coll.read_preference)
        self.assertEqual(self.db_session.codec_options, coll.codec_options)
        self.assertEqual(self.db_session.write_concern, coll.write_concern)