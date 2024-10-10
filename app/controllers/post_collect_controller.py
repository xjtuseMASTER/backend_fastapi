from typing import Optional
from app.core.crud import CRUDBase
from app.models.post import PostCollect
from app.schemas.post_collect_schemas import PostCollectCreate, PostCollectUpdate


class PostCollectController(CRUDBase[PostCollect, PostCollectCreate, PostCollectUpdate]):
    def __init__(self):
        super().__init__(model=PostCollect)

    async def get_collects_by_post_id(self, post_id: int) -> Optional[list["PostCollect"]]:
        return await self.model.filter(to_post_id=post_id).all()


post_collect_controller = PostCollectController()
