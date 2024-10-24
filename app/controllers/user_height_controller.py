from app.models.post import UserHeight
from app.core.crud import CRUDBase
from app.schemas.user_height import *
from tortoise.exceptions import *
from typing import List


class UserHeightController(CRUDBase[UserHeight,UserHeightCreate,UserHeightUpadate]):
    def __init__(self):
        super().__init__(model=UserHeight)

    async def get_user_heights(self, user_id: str) -> List["UserHeight"]:
        return await self.model.all().filter(user_id=user_id).order_by("-record_date").offset(0).limit(5)


    


user_height_controller = UserHeightController()