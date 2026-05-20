from pydantic import BaseModel
from typing import Optional
from datetime import date

class PlayerCreate(BaseModel):
    name:str
    position:str
    team:str

class StatCreate(BaseModel):
    player_id:int
    opponent:str
    points:int
    rebounds:int
    assists:int
    game_date:date

class PlayerUpdate(BaseModel):
    name:Optional[str] = None
    position:Optional[str] = None
    team:Optional[str] = None
