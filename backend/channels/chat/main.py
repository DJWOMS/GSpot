from fastapi import FastAPI
from src.router import router
from services.database import db


app = FastAPI()

app.include_router(router)


@app.on_event('startup')
async def init_db():
    db.session = await db.client.start_session()
