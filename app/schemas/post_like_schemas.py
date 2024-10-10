from pydantic import BaseModel, Field

class BasePostLike(BaseModel):
    like_id: int
    user_id: int
    to_post_id: int
    create_time: str

class PostLikeCreate(BaseModel):
    user_id: int = Field(example=1, description="点赞用户ID")
    to_post_id: int = Field(example=1, description="被点赞的帖子ID")

class PostLikeUpdate(BaseModel):
    like_id: int
