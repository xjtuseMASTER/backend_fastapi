from typing import Optional,List
from app.core.crud import CRUDBase
from app.models.post import PostCollect
from app.schemas.post_collect_schemas import PostCollectCreate, PostCollectUpdate


class PostCollectController(CRUDBase[PostCollect, PostCollectCreate, PostCollectUpdate]):
    def __init__(self):
        super().__init__(model=PostCollect)

    async def get_collects_by_post_id(self, post_id: int) -> Optional[list["PostCollect"]]:
        return await self.model.filter(to_post_id=post_id).all()
    
    
    async def get_user_collect(self,user_id:str,pageNumber:int) -> List["PostCollect"]:
        # 每页20条数据，计算偏移量
        limit = 20
        offset = (pageNumber - 1) * limit
        return await self.model.filter(user_id=user_id).offset(offset).limit(limit)


post_collect_controller = PostCollectController()
