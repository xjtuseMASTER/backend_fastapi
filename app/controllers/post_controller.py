from typing import Optional
from typing import List
from app.core.crud import CRUDBase
from app.models.post import Post
from app.schemas.post_schemas import PostCreate, PostUpdate


class PostController(CRUDBase[Post, PostCreate, PostUpdate]):
    def __init__(self):
        super().__init__(model=Post)

    async def get_by_title(self, title: str) -> Optional["Post"]:
        return await self.model.filter(title=title).first()
    
    
    
    async def get_posts(self, pageNumber: int) -> List["Post"]:
        # 每页 20 条，计算起始位置
        offset = (pageNumber - 1) * 20
        return await self.model.all().order_by("-create_time").offset(offset).limit(20)
    
    
    async def get_user_own_posts(self,user_id:str,pageNumber:int) -> List["Post"]:
        # 每页20条数据，计算偏移量
        limit = 20
        offset = (pageNumber - 1) * limit
        return await self.model.filter(user_id=user_id).offset(offset).limit(limit)


post_controller = PostController()
