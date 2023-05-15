from fastapi import FastAPI
from core.router import router
from core.database import db


app = FastAPI()

app.include_router(router)


@app.on_event('startup')
async def init_db():
    db.session = await db.client.start_session()
