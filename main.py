from fastapi import FastAPI
from db import models
from db.database import engine  # Add this import to get the engine
from routers import user

app = FastAPI()

app.include_router(user.router)
models.Base.metadata.create_all(bind=engine)


@app.get("/")
def hw():
    return {"message": "Hello World"}
