from fastapi import APIRouter, Query
from app.controllers.follower_controller import follower_controller
from app.schemas import Success
from app.schemas.follower_schemas import FollowerCreate, FollowerUpdate

router = APIRouter()

@router.get("/list", summary="查看关注列表")
async def list_followers(user_id: int = Query(None, description="用户ID")):
    followers = await follower_controller.get_followers_by_user_id(user_id)
    return Success(data=followers)

@router.get("/get", summary="查看关注")
async def get_follower(id: int = Query(..., description="关注ID")):
    follower = await follower_controller.get(id=id)
    return Success(data=follower)

@router.post("/create", summary="创建关注")
async def create_follower(follower_in: FollowerCreate):
    await follower_controller.create_follower(obj_in=follower_in)
    return Success(msg="Created Successfully")

@router.post("/update", summary="更新关注")
async def update_follower(follower_in: FollowerUpdate):
    await follower_controller.update_follower(obj_in=follower_in)
    return Success(msg="Updated Successfully")

@router.delete("/delete", summary="删除关注")
async def delete_follower(id: int = Query(..., description="关注ID")):
    await follower_controller.delete_follower(follower_id=id)
    return Success(msg="Deleted Successfully")
