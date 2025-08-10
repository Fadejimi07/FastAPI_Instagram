from sqlalchemy.orm import Session
from db.models import DbUser
from routers.schemas import UserBase
from db.hashing import Hash
from fastapi import HTTPException


def create_user(db: Session, request: UserBase):
    new_user = DbUser(
        email=request.email,
        username=request.username,
        password=Hash.bcrypt(request.password),
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    if not new_user:
        raise HTTPException(status_code=400, detail="User creation failed")
    return new_user

def get_all_users(db: Session):
    users = db.query(DbUser).all()
    if not users:
        raise HTTPException(status_code=404, detail="No users found")
    return users

def get_user(db: Session, user_id: int):
    user = db.query(DbUser).filter(DbUser.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
