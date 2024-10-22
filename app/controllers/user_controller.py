from app.models.post import User
from app.core.crud import CRUDBase
from app.schemas.user_schemas import *
from tortoise.exceptions import *

class UserController(CRUDBase[User,UserCreate,UserUpdate]):
    def __init__(self):
        super().__init__(model=User)
    
    
    async def get_user(self,user_id:str):
        return await User.get(user_id=user_id)
    
    async def update_user_in_db(self,user: UserUpdateRequest) -> bool:
        try:
            # 查询用户是否存在
            existing_user = await User.get(user_id=user.user_id)
        except DoesNotExist:
            return False  # 如果用户不存在，返回 False

        # 更新非空字段的数据
        update_data = user.dict(exclude_unset=True)
        for key, value in update_data.items():
            setattr(existing_user, key, value)

        # 保存更新后的用户信息
        await existing_user.save()
        return True  # 更新成功
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    async def get(self, id: int):
        return await User.get_or_none(user_id=id)

    async def get_users_by_name(self, name: str):
        if name:
            return await User.filter(user_name__contains=name).all()
        return await User.all()

    async def create_user(self, obj_in):
        return await User.create(**obj_in.dict())

    async def update_user(self, obj_in):
        user = await User.get_or_none(user_id=obj_in.user_id)
        if user:
            user.update_from_dict(obj_in.dict(exclude_unset=True))
            await user.save()
            return user
        return None

    async def delete_user(self, user_id: int):
        user = await User.get_or_none(user_id=user_id)
        if user:
            await user.delete()
            return True
        return False
    
    



user_controller = UserController()
