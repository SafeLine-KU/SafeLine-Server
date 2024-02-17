from fastapi import FastAPI
from dotenv import load_dotenv

from routers import instruction, safezone

app = FastAPI()
load_dotenv()

app.include_router(instruction.router)
app.include_router(safezone.router)