from fastapi import APIRouter,HTTPException
from schemas import PlayerCreate
from database import conn,cursor

router = APIRouter()

@router.post("/players")
def create_player(player:PlayerCreate):
    cursor.execute("INSERT INTO players (name,position,team) VALUES(%s,%s,%s)", (player.name,player.position,player.team))
    conn.commit()
    return{"message":"Player created"}

@router.get("/players/{player_id}")
def get_player(player_id:int):
    cursor.execute("SELECT * FROM PLAYERS WHERE ID = %s",(player_id,))
    player = cursor.fetchone()
    if not player:
        raise HTTPException(status_code = 404, detail = "Player not found")
    return player

@router.delete("/players/{player_id}")
def delete_player(player_id:int):
    cursor.execute("DELETE FROM PLAYERS WHERE ID = %s",(player_id,))
    conn.commit()
    if cursor.rowcount==0:
        raise HTTPException(status = 404, 
                            detail="Player not found!")
    else:
        return {"message":"Player successfully deleted"}
    

    

