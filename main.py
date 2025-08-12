from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from db import models
from db.database import engine  # Add this import to get the engine
from routers import user, post
from auth import authentication as auth

app = FastAPI()

app.include_router(user.router)
app.include_router(post.router)
app.include_router(auth.router)

models.Base.metadata.create_all(bind=engine)


@app.get("/")
def hw():
    return {"message": "Hello World"}


app.mount("/images", StaticFiles(directory="images"), name="images")
