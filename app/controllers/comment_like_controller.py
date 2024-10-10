from typing import Optional
from app.core.crud import CRUDBase
from app.models.post import CommentLike
from app.schemas.comment_like_schemas import CommentLikeCreate, CommentLikeUpdate


class CommentLikeController(CRUDBase[CommentLike, CommentLikeCreate, CommentLikeUpdate]):
    def __init__(self):
        super().__init__(model=CommentLike)

    async def get_likes_by_comment_id(self, comment_id: int) -> Optional[list["CommentLike"]]:
        return await self.model.filter(to_comment_id=comment_id).all()


comment_like_controller = CommentLikeController()
