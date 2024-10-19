from typing import Optional
from app.core.crud import CRUDBase
from app.models.post import Comment
from app.schemas.comment_schemas import CommentCreate, CommentUpdate


class CommentController(CRUDBase[Comment, CommentCreate, CommentUpdate]):
    def __init__(self):
        super().__init__(model=Comment)
        
    async def get_comment(self,comment_id:str):
        return await Comment.get(comment_id=comment_id)



comment_controller = CommentController()
