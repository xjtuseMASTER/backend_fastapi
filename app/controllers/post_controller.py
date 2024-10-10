from typing import Optional
from app.core.crud import CRUDBase
from app.models.post import Post
from app.schemas.post_schemas import PostCreate, PostUpdate


class PostController(CRUDBase[Post, PostCreate, PostUpdate]):
    def __init__(self):
        super().__init__(model=Post)

    async def get_by_title(self, title: str) -> Optional["Post"]:
        return await self.model.filter(title=title).first()


post_controller = PostController()
