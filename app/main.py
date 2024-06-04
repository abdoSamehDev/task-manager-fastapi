from fastapi import FastAPI
from .database import engine
from . import models
from .routes import user, task

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
async def welcome():
    return {"status": "ok", "message": "Welcome to Task Manager"}


@app.get("/status")
async def get_status():
    return {"status": "ok", "message": "Application is running smoothly"}


app.include_router(user.router, tags=["Auth"])
app.include_router(task.router, prefix="/tasks", tags=["Tasks"])
