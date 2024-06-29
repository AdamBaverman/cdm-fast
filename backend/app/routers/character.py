from fastapi import APIRouter, Depends, HTTPException
from typing import List
from app.crud.character import get_characters, get_character, create_character, update_character, delete_character
from app.models.character import character_collection
from app.schemas.character import Character, CharacterCreate
from dependencies import get_database

router = APIRouter(
    prefix="/characters",
    tags=["characters"],
    responses={404: {"description": "Not found"}},
)

@router.get("/", response_model=List[Character])
def read_characters(db = Depends(get_database)):
    return get_characters(db.characters)

@router.get("/{character_id}", response_model=Character)
def read_character(character_id: str, db = Depends(get_database)):
    character = get_character(db.characters, character_id)
    if character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return character

@router.post("/", response_model=Character)
def create_new_character(character: CharacterCreate, db = Depends(get_database)):
    return create_character(db.characters, character)

@router.put("/{character_id}", response_model=Character)
def update_existing_character(character_id: str, character: CharacterCreate, db = Depends(get_database)):
    updated_character = update_character(db.characters, character_id, character)
    if updated_character is None:
        raise HTTPException(status_code=404, detail="Character not found")
    return updated_character

@router.delete("/{character_id}")
def delete_existing_character(character_id: str, db = Depends(get_database)):
    delete_character(db.characters, character_id)
    return {"message": "Character deleted"}
