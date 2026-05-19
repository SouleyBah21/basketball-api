from fastapi import APIRouter,HTTPException
from schemas import PlayerCreate
from database import conn,cursor

router = APIRouter()

@router.post("/players")
def create_player(player:PlayerCreate):
    cursor.execute("INSERT INTO players (name,position,team) VALUES(%s,%s,%s)", (player.name,player.position,player.team))
    conn.commit()
    return{"message":"Player created"}


