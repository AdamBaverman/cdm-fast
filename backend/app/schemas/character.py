from pydantic import BaseModel

class CharacterBase(BaseModel):
    full_name: str
    age: int
    gender: str

class CharacterCreate(CharacterBase):
    pass

class Character(CharacterBase):
    id: str

    class Config:
        orm_mode = True
