from pymongo import MongoClient
from pymongo.collection import Collection


def get_mongo_db_collection() -> Collection:
    client = MongoClient('character-sheet-db', 27017)
    database = client.get_database('dnd')
    return database.get_collection('characterSheet')
