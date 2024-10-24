from typing import *
from app.core.crud import CRUDBase
from app.models.post import UserWeight
from app.schemas.user_weight_schema import *

class UserWeightController(CRUDBase[UserWeight, UserWeightCreate, UserWeightUpdate]):
    def __init__(self):
        super().__init__(model=UserWeight)

    
    async def get_user_weights(self, user_id: str) -> List["UserWeight"]:
        return await self.model.all().filter(user_id=user_id).order_by("-record_date").offset(0).limit(5)




user_weight_controller = UserWeightController()