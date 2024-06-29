from typing import List
from bson import ObjectId
from pymongo.collection import Collection
from schemas.character import CharacterCreate, Character

def get_characters(collection: Collection) -> List[Character]:
    characters = list(collection.find())
    return [Character(**character, id=str(character["_id"])) for character in characters]

def get_character(collection: Collection, character_id: str) -> Character:
    character = collection.find_one({"_id": ObjectId(character_id)})
    if character:
        return Character(**character, id=str(character["_id"]))
    return None

def create_character(collection: Collection, character: CharacterCreate) -> Character:
    result = collection.insert_one(character.dict())
    return Character(**character.dict(), id=str(result.inserted_id))

def update_character(collection: Collection, character_id: str, character: CharacterCreate) -> Character:
    collection.update_one({"_id": ObjectId(character_id)}, {"$set": character.dict()})
    return get_character(collection, character_id)

def delete_character(collection: Collection, character_id: str):
    collection.delete_one({"_id": ObjectId(character_id)})
