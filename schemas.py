from pydantic import BaseModel
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
