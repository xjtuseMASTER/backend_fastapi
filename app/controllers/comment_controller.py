from typing import Optional
from app.core.crud import CRUDBase
from app.models.post import Comment
from app.schemas.comment_schemas import CommentCreate, CommentUpdate


class CommentController(CRUDBase[Comment, CommentCreate, CommentUpdate]):
    def __init__(self):
        super().__init__(model=Comment)

    async def get_by_post_id(self, post_id: int) -> Optional["Comment"]:
        return await self.model.filter(post_id=post_id).all()


comment_controller = CommentController()
