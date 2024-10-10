from pydantic import BaseModel, Field

class BaseCommentLike(BaseModel):
    like_id: int
    user_id: int
    to_comment_id: int
    create_time: str

class CommentLikeCreate(BaseModel):
    user_id: int = Field(example=1, description="点赞用户ID")
    to_comment_id: int = Field(example=1, description="被点赞的评论ID")

class CommentLikeUpdate(BaseModel):
    like_id: int
