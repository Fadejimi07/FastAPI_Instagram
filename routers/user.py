from fastapi import APIRouter, Depends, HTTPException
from schemas import UserBase  # Adjust the import path as needed
from sqlalchemy.orm import Session
from db.database import get_db
from db import db_user  # Adjust the import path as needed

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=UserBase)
def create_user(request: UserBase, db: Session = Depends(get_db)):
    return db_user.create_user(db, request)


@router.get("/", response_model=list[UserBase])
def get_all_users(db: Session = Depends(get_db)):
    return db_user.get_all_users(db)


@router.get("/{user_id}", response_model=UserBase)
def get_user(user_id: int, db: Session = Depends(get_db)):
    return db_user.get_user(db, user_id)
