from pydantic import BaseModel, Field
from typing import Optional

class BaseComment(BaseModel):
    comment_id: int
    post_id: int
    user_id: int
    content: str
    father_comment_id: Optional[int]
    level: int
    likes_num: int
    creat_time: str

class CommentCreate(BaseModel):
    post_id: int = Field(example=1, description="关联的帖子ID")
    user_id: int = Field(example=1, description="用户ID")
    content: str = Field(example="This is a comment content", description="评论内容")
    father_comment_id: Optional[int] = Field(example=0, description="父评论ID")

class CommentUpdate(BaseModel):
    comment_id: int
    content: Optional[str] = Field(example="Updated comment content.")
