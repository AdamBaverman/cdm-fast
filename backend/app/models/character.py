from pymongo import MongoClient

client = MongoClient('mongodb://mongo:27017')
db = client.fantasy_world

character_collection = db.characters

# Инициализация коллекции при первом запуске
if 'characters' not in db.list_collection_names():
    db.create_collection('characters')
