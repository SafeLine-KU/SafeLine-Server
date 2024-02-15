from fastapi import FastAPI

from routers import instruction, safezone

app = FastAPI()

app.include_router(instruction.router)
app.include_router(safezone.router)