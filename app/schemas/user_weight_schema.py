from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class BaseUserWeight(BaseModel):
    user_id : str
    weight : float
    record_date : Optional[datetime]

class UserWeightCreate(BaseModel):
    user_id : str
    weight : float


class UserWeightUpdate(BaseModel):
    pass