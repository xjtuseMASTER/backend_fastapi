from typing import *
from app.core.crud import CRUDBase
from app.models.post import UserHeight
from app.schemas.user_height_schemas import *

class UserHeightController(CRUDBase[UserHeight, UserHeightCreate, UserHeightUpdate]):
    def __init__(self):
        super().__init__(model=UserHeight)

    async def get_likes_by_post_id(self, post_id: int) -> Optional[list["UserHeight"]]:
        return await self.model.filter(to_post_id=post_id).all()
    
    
    async def get_user_likes(self,user_id:str,pageNumber:int) -> List["UserHeight"]:
        # 每页20条数据，计算偏移量
        limit = 20
        offset = (pageNumber - 1) * limit
        return await self.model.filter(user_id=user_id).offset(offset).limit(limit)
    
    async def get_user_likes(self,user_id:str,pageNumber:int) -> List["UserHeight"]:
        # 每页20条数据，计算偏移量
        limit = 20
        offset = (pageNumber - 1) * limit
        return await self.model.filter(user_id=user_id).offset(offset).limit(limit)
    
    
    
    async def get_user_heights(self, user_id: str) -> List["UserHeight"]:
        return await self.model.all().filter(user_id=user_id).order_by("-record_date").offset(0).limit(5)


user_height_controller = UserHeightController()