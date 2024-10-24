from pydantic import BaseModel, Field

class BaseUserHeight(BaseModel):
    pictures_id: int
    to_post_id: int
    sequence: int
    position: str

class UserHeightCreate(BaseModel):
    pass

class UserHeightUpdate(BaseModel):
    pass
