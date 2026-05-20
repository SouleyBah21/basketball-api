from fastapi import APIRouter,HTTPException
from schemas import PlayerCreate,PlayerUpdate
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
        raise HTTPException(status_code = 404, 
                            detail="Player not found!")
    else:
        return {"message":"Player successfully deleted"}
    
@router.get("/players")
def get_players():
    cursor.execute("SELECT * FROM PLAYERS")
    players = cursor.fetchall()
    return players
@router.patch("/players/{player_id}")
def update_player(player_id:int,updated_player:PlayerUpdate):
    updated_data = updated_player.model_dump(exclude_unset=True)
    if not updated_data:
        raise HTTPException(status_code = 404,detail="No fields provided!")
    set_clause = ", ".join([f"{field} = %s" for field in updated_data.keys()])
    values = list(updated_data.values())
    values.append(player_id)

    cursor.execute(
        f"UPDATE players SET {set_clause} WHERE id = %s",
        values
    )

    conn.commit()

    if cursor.rowcount == 0:
        raise HTTPException(status_code=404, detail="Player not found")

    return {"message": "Player updated"}
@router.put("/players/{player_id}")
def replace_player(player_id:int,updated_player:PlayerUpdate):
    cursor.execute("UPDATE PLAYERS  SET name = %s,position = %s, team = %s WHERE ID = %s",(updated_player.name,updated_player.position,updated_player.team,player_id,))
    conn.commit()
    if cursor.rowcount==0:
        raise HTTPException(status_code = 404, detail = "Player not found")
    return{"message":"Player replaced"}



    
    
    

    

    

