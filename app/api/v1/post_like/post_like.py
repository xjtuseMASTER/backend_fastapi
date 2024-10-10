from fastapi import APIRouter, Query
from app.controllers.post_like_controller import post_like_controller
from app.schemas import Success
from app.schemas.post_like_schemas import PostLikeCreate

router = APIRouter()

@router.post("/create", summary="创建帖子点赞")
async def create_post_like(like_in: PostLikeCreate):
    await post_like_controller.create_post_like(obj_in=like_in)
    return Success(msg="Created Successfully")

@router.delete("/delete", summary="删除帖子点赞")
async def delete_post_like(id: int = Query(..., description="点赞ID")):
    await post_like_controller.delete_post_like(like_id=id)
    return Success(msg="Deleted Successfully")
