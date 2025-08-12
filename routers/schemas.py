from pydantic import BaseModel
from typing import List


class Post(BaseModel):
    title: str
    content: str
    image_url: str
    timestamp: str

    class Config:
        from_attributes = True


class UserBase(BaseModel):
    username: str
    email: str
    password: str


class UserDisplay(BaseModel):
    username: str
    email: str
    posts: List["Post"] = []

    class Config:
        from_attributes = True


class User(BaseModel):
    username: str
    email: str

    class Config:
        from_attributes = True



class PostBase(BaseModel):
    title: str
    content: str
    image_url: str
    creator_id: int


class PostDisplay(BaseModel):
    title: str
    content: str
    image_url: str
    creator: User

    class Config:
        from_attributes = True


class CommentBase(BaseModel):
    content: str
    post_id: int
    user_id: int


class CommentDisplay(BaseModel):
    content: str
    created_at: str
    post: Post
    user: User

    class Config:
        from_attributes = True
