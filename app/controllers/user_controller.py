from app.models.post import User

class UserController:
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
