from typing import Optional
from app.core.crud import CRUDBase
from app.models.post import Follower
from app.schemas.follower_schemas import FollowerCreate, FollowerUpdate


class FollowerController(CRUDBase[Follower, FollowerCreate, FollowerUpdate]):
    def __init__(self):
        super().__init__(model=Follower)

    async def get_followers_by_user_id(self, user_id: int) -> Optional[list["Follower"]]:
        return await self.model.filter(to_user_id=user_id).all()


follower_controller = FollowerController()
