from pymongo import MongoClient
from config import settings

def get_database():
    client = MongoClient(settings.MONGO_URL)
    db = client.fantasy_world
    return db
