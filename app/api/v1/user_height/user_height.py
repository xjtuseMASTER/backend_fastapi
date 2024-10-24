
from fastapi import APIRouter, Query
from app.controllers.user_height_comtroller import user_height_controller
from app.schemas import Success
from app.schemas.user_height_schemas import *

router = APIRouter()


@router.get("/getheightlist", summary="创建帖子点赞")
async def create_post_like(userId: str = Query(..., description="用户ID")):
    heights=await user_height_controller.get_user_heights(user_id=userId)
    return Success(data= [await height.to_dict() for height in heights])



@router.post("/create", summary="创建帖子点赞")
async def create_post_like(like_in: UserHeightCreate):
    await post_like_controller.create_post_like(obj_in=like_in)
    return Success(msg="Created Successfully")

@router.delete("/delete", summary="删除帖子点赞")
async def delete_post_like(id: int = Query(..., description="点赞ID")):
    await post_like_controller.delete_post_like(like_id=id)
    return Success(msg="Deleted Successfully")


@router.get("/like", summary="用户查看收藏记录")
async def get_user_collect(
    userId: str = Query(..., description="用户ID"),
    pageNumber: int = Query(..., description="分页处理，第20条数据一页")
):
    print("用户查看收藏记录")

    # 查询数据库，获取用户收藏数据
    collects = await post_like_controller.get_user_likes(user_id=userId,pageNumber=pageNumber)
    # 返回成功响应
    return Success(data=[await collect.to_dict() for collect in collects])
