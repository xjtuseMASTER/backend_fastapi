from fastapi import APIRouter, Query
from app.controllers.post_controller import post_controller
from app.schemas import Success
from app.schemas.post_schemas import PostCreate, PostUpdate

router = APIRouter()

@router.get("/stream", summary="查看帖子")
async def getposts(pageNumber: int = Query(..., description="页码id"),user_id : int | None = None):
    posts = await post_controller.get_posts(pageNumber)
    print("get")
    return Success(data= [await post.to_dict() for post in posts])


@router.get("/mypost", summary="用户查看自己的发帖")
async def get_user_collect(
    userId: str = Query(..., description="用户ID"),
    pageNumber: int = Query(..., description="分页处理，第20条数据一页")
):
    print("用户查看收藏记录")

    # 查询数据库，获取用户收藏数据
    collects = await post_controller.get_user_own_posts(user_id=userId,pageNumber=pageNumber)
    # 返回成功响应
    return Success(data=[await collect.to_dict() for collect in collects])





@router.get("/list", summary="查看帖子列表")
async def list_posts(title: str = Query(None, description="帖子标题")):
    posts = await post_controller.get_posts_by_title(title)
    return Success(data=posts)

@router.get("/get", summary="查看帖子")
async def get_post(id: int = Query(..., description="帖子ID")):
    post = await post_controller.get(id=id)
    return Success(data=post)

@router.post("/create", summary="创建帖子")
async def create_post(post_in: PostCreate):
    await post_controller.create_post(obj_in=post_in)
    return Success(msg="Created Successfully")

@router.post("/update", summary="更新帖子")
async def update_post(post_in: PostUpdate):
    await post_controller.update_post(obj_in=post_in)
    return Success(msg="Updated Successfully")

@router.delete("/delete", summary="删除帖子")
async def delete_post(id: int = Query(..., description="帖子ID")):
    await post_controller.delete_post(post_id=id)
    return Success(msg="Deleted Successfully")
