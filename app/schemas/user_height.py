from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BaseUserHeight(BaseModel):
    user_id : str
    height : float
    record_date : Optional[datetime]

class UserHeightCreate(BaseModel):
    user_id : str
    height : float


class UserHeightUpadate(BaseModel):
    pass