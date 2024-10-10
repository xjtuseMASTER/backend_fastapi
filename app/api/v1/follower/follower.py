import logging
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.post import Follower
from app.schemas.follower_schemas import FollowerCreate, FollowerUpdate, BaseFollower

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/", response_model=BaseFollower, summary="创建关注", description="根据提供的关注信息创建一个新的关注记录")
async def create_follower(follower: FollowerCreate):
    new_follower = await Follower.create(**follower.dict())
    return new_follower

@router.get("/", response_model=List[BaseFollower], summary="获取所有关注", description="返回数据库中所有关注记录的信息")
async def get_all_followers():
    return await Follower.all()

@router.get("/{follower_id}", response_model=BaseFollower, summary="获取指定关注", description="根据关注ID获取特定关注记录")
async def get_follower_by_id(follower_id: int):
    follower = await Follower.get_or_none(follower_id=follower_id)
    if not follower:
        raise HTTPException(status_code=404, detail="Follower not found")
    return follower

@router.put("/{follower_id}", response_model=BaseFollower, summary="更新关注信息", description="根据关注ID更新关注的基本信息")
async def update_follower(follower_id: int, follower_data: FollowerUpdate):
    follower = await Follower.get_or_none(follower_id=follower_id)
    if not follower:
        raise HTTPException(status_code=404, detail="Follower not found")
    follower.update_from_dict(follower_data.dict(exclude_unset=True))
    await follower.save()
    return follower

@router.delete("/{follower_id}", response_model=dict, summary="删除关注", description="根据关注ID删除关注信息")
async def delete_follower(follower_id: int):
    follower = await Follower.get_or_none(follower_id=follower_id)
    if not follower:
        raise HTTPException(status_code=404, detail="Follower not found")
    await follower.delete()
    return {"message": "Follower deleted successfully"}
