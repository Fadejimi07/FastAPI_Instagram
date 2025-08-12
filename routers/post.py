from fastapi import APIRouter, Body, Depends, File, Form, HTTPException, UploadFile
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_post, db_user
from routers.schemas import (
    PostDisplay,
)  # Adjust the import path as needed
from auth.oauth2 import get_current_user
from util.helpers import save_image

router = APIRouter(prefix="/posts", tags=["posts"])


@router.post("/", response_model=PostDisplay)
def create_post(
    title: str = Form(...),
    content: str = Form(...),
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
    image: UploadFile = File(...),
):
    image_url = save_image(image)
    if not image_url:
        raise HTTPException(status_code=400, detail="Image upload failed")

    return db_post.create_post(db, title, content, current_user.id, image_url)


@router.get("/", response_model=list[PostDisplay])
def get_all_posts(db: Session = Depends(get_db)):
    return db_post.get_all_posts(db)


@router.get("/user_posts", response_model=list[PostDisplay])
def get_user_posts(
    db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    return db_post.get_user_posts(db, current_user.id)


@router.get("/delete/{post_id}")
def delete_post(
    post_id: int, db: Session = Depends(get_db), current_user=Depends(get_current_user)
):
    return db_post.delete_post(db, post_id, current_user.id)
