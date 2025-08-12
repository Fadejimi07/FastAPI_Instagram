from sqlalchemy.orm import Session
from db.models import DbPost
from fastapi import HTTPException, status


def create_post(db: Session, title: str, content: str, user_id: int, image_url: str):
    new_post = DbPost(
        title=title,
        content=content,
        user_id=user_id,
        image_url=image_url,
    )

    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    if not new_post:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Post creation failed"
        )
    return new_post


def get_all_posts(db: Session):
    posts = db.query(DbPost).all()
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No posts found"
        )
    return posts


def get_user_posts(db: Session, user_id: int):
    posts = db.query(DbPost).filter(DbPost.user_id == user_id).all()
    if not posts:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No posts found for this user"
        )
    return posts


def delete_post(db: Session, post_id: int, user_id: int):
    post = (
        db.query(DbPost).filter(DbPost.id == post_id, DbPost.user_id == user_id).first()
    )
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Post not found"
        )
    db.delete(post)
    db.commit()
    return {"detail": "Post deleted successfully"}
