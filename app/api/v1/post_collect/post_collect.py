from fastapi import APIRouter, Query
from app.controllers.post_collect_controller import post_collect_controller
from app.schemas import Success
from app.schemas.post_collect_schemas import PostCollectCreate

router = APIRouter()

@router.post("/create", summary="创建帖子收藏", description="根据提供的信息创建一个新的帖子收藏记录")
async def create_post_collect(collect_in: PostCollectCreate):
    await post_collect_controller.create_post_collect(obj_in=collect_in)
    return Success(msg="Created Successfully")

@router.delete("/delete", summary="删除帖子收藏", description="根据收藏ID删除指定的帖子收藏记录")
async def delete_post_collect(id: int = Query(..., description="帖子收藏ID")):
    await post_collect_controller.delete_post_collect(collect_id=id)
    return Success(msg="Deleted Successfully")

@router.get("/collect", summary="用户查看收藏记录")
async def get_user_collect(
    userId: str = Query(..., description="用户ID"),
    pageNumber: int = Query(..., description="分页处理，第20条数据一页")
):
    print("用户查看收藏记录")

    # 查询数据库，获取用户收藏数据
    collects = await post_collect_controller.get_user_collect(user_id=userId,pageNumber=pageNumber)
    # 返回成功响应
    return Success(data=[await collect.to_dict() for collect in collects])

