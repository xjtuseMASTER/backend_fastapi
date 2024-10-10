from pydantic import BaseModel, Field

class BaseFollower(BaseModel):
    follower_id: int
    to_user_id: int
    follow_each_other: bool

class FollowerCreate(BaseModel):
    follower_id: int = Field(example=1, description="关注者用户ID")
    to_user_id: int = Field(example=2, description="被关注的用户ID")
    follow_each_other: bool = Field(default=False, description="是否互相关注")

class FollowerUpdate(BaseModel):
    follower_id: int
    follow_each_other: bool = Field(example=True, description="是否互相关注")
