import logging

from fastapi import APIRouter, HTTPException
from typing import List
from app.models.post import User
from app.schemas.user_schemas import UserCreate, UserUpdate, BaseUser


logger = logging.getLogger(__name__)

router = APIRouter()

# 创建用户接口
@router.post("/", response_model=BaseUser, summary="创建用户", description="根据提供的用户信息创建一个新的用户")
async def create_user(user: UserCreate):
    new_user = await User.create(**user.dict())  # 使用User模型创建新用户
    return new_user

# 获取所有用户接口
@router.get("/", response_model=List[BaseUser], summary="获取所有用户", description="返回数据库中所有用户的信息")
async def get_all_users():
    return await User.all()

# 根据ID获取用户接口
@router.get("/{user_id}", response_model=BaseUser, summary="获取指定用户", description="根据用户ID获取特定用户信息")
async def get_user_by_id(user_id: int):
    user = await User.get_or_none(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# 更新用户接口
@router.put("/{user_id}", response_model=BaseUser, summary="更新用户信息", description="根据用户ID更新用户的基本信息")
async def update_user(user_id: int, user_data: UserUpdate):
    user = await User.get_or_none(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    user.update_from_dict(user_data.dict(exclude_unset=True))
    await user.save()
    return user

# 删除用户接口
@router.delete("/{user_id}", response_model=dict, summary="删除用户", description="根据用户ID删除用户信息")
async def delete_user(user_id: int):
    user = await User.get_or_none(user_id=user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    await user.delete()
    return {"message": "User deleted successfully"}
