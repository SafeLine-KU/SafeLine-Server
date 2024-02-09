from contextlib import asynccontextmanager
from fastapi import FastAPI

from models.db import mongodb

@asynccontextmanager
async def lifespan(app: FastAPI):
    mongodb.connect()
    yield
    mongodb.close()

app = FastAPI(lifespan=lifespan)
