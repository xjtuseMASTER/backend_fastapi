from pydantic import BaseModel, Field
from typing import Optional

class BasePost(BaseModel):
    post_id: int
    user_id: int
    title: str
    content: str
    create_time: str
    update_time: str
    likes_num: int
    collects_num: int
    comments_num: int

class PostCreate(BaseModel):
    user_id: int = Field(example=1, description="用户ID")
    title: str = Field(example="This is a post title", description="帖子标题")
    content: str = Field(example="This is post content.", description="帖子内容")

class PostUpdate(BaseModel):
    post_id: int
    title: Optional[str] = Field(example="Updated post title")
    content: Optional[str] = Field(example="Updated post content.")
