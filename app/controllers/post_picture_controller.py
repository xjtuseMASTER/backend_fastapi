from typing import Optional
from app.core.crud import CRUDBase
from app.models.post import PostPicture
from app.schemas.post_picture_schemas import PostPictureCreate, PostPictureUpdate


class PostPictureController(CRUDBase[PostPicture, PostPictureCreate, PostPictureUpdate]):
    def __init__(self):
        super().__init__(model=PostPicture)

    async def get_pictures_by_post_id(self, post_id: int) -> Optional[list["PostPicture"]]:
        return await self.model.filter(to_post_id=post_id).all()


post_picture_controller = PostPictureController()
