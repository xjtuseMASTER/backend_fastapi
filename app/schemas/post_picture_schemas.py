from pydantic import BaseModel, Field

class BasePostPicture(BaseModel):
    pictures_id: int
    to_post_id: int
    sequence: int
    position: str

class PostPictureCreate(BaseModel):
    to_post_id: int = Field(example=1, description="关联的帖子ID")
    sequence: int = Field(example=1, description="图片顺序")
    position: str = Field(example="top-left", description="图片位置")

class PostPictureUpdate(BaseModel):
    pictures_id: int
