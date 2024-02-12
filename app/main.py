from contextlib import asynccontextmanager
from fastapi import FastAPI

from models.db import mongodb
from routers import instruction, safezone

@asynccontextmanager
async def lifespan(app: FastAPI):
    mongodb.connect()
    yield
    mongodb.close()

app = FastAPI(lifespan=lifespan)

app.include_router(instruction.router)
app.include_router(safezone.router)