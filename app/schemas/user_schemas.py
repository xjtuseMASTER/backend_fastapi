from enum import StrEnum
from typing import Optional
from pydantic import BaseModel, Field

class GenderType(StrEnum):
    MALE = "male"
    FEMALE = "female"
    OTHER = "other"

class BaseUser(BaseModel):
    user_id: int
    email: str
    user_name: str
    avatar: Optional[str]
    likes_num: int
    birthday: Optional[str]
    selfIntro: Optional[str]
    gender: Optional[GenderType]
    followers_num: int
    collects_num: int

class UserCreate(BaseModel):
    user_id : int = Field(examples=123)
    email: str = Field(example="example@domain.com")
    password: str = Field(example="yourpassword")
    user_name: str = Field(example="John Doe")
    avatar: Optional[str] = Field(default=None)
    gender: Optional[GenderType] = Field(example=GenderType.MALE.value)
    selfIntro: Optional[str] = Field(example="This is my introduction.")

class UserUpdate(BaseModel):
    user_id: int
    user_name: Optional[str] = Field(example="John Doe")
    avatar: Optional[str] = Field(default=None)
    gender: Optional[GenderType] = Field(example=GenderType.FEMALE.value)
    selfIntro: Optional[str] = Field(example="Updated introduction.")
    
class UserUpdateRequest(BaseModel):
    user_id: str
    user_name: Optional[str] = None
    gender: Optional[str] = None
    birthday: Optional[str] = None
    selfIntro: Optional[str] = None
