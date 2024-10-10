from typing import Optional
from app.core.crud import CRUDBase
from app.models.post import PostLike
from app.schemas.post_like_schemas import PostLikeCreate, PostLikeUpdate


class PostLikeController(CRUDBase[PostLike, PostLikeCreate, PostLikeUpdate]):
    def __init__(self):
        super().__init__(model=PostLike)

    async def get_likes_by_post_id(self, post_id: int) -> Optional[list["PostLike"]]:
        return await self.model.filter(to_post_id=post_id).all()


post_like_controller = PostLikeController()

