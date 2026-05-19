from fastapi import FastAPI
from routers.players import router as player_router

app = FastAPI()
app.include_router(player_router)
