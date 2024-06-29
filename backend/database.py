from pymongo import MongoClient
from config import settings

client = MongoClient(settings.MONGO_URL)
db = client.fantasy_world

character_collection = db.characters

# Инициализация коллекции при первом запуске
if 'characters' not in db.list_collection_names():
    db.create_collection('characters')
