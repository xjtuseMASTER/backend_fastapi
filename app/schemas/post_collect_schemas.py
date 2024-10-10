from pydantic import BaseModel, Field

class BasePostCollect(BaseModel):
    collect_id: int
    user_id: int
    to_post_id: int
    create_time: str

class PostCollectCreate(BaseModel):
    user_id: int = Field(example=1, description="收藏用户ID")
    to_post_id: int = Field(example=1, description="被收藏的帖子ID")

class PostCollectUpdate(BaseModel):
    collect_id: int
