from pydantic import BaseModel


class Character(BaseModel):
    name: str
    max_hp: int = None
