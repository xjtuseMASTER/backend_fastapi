from fastapi import APIRouter, Query
from app.controllers.post_picture_controller import post_picture_controller
from app.schemas import Success
from app.schemas.post_picture_schemas import PostPictureCreate

router = APIRouter()

@router.post("/create", summary="上传帖子图片", description="根据提供的信息上传一张新的帖子图片")
async def create_post_picture(picture_in: PostPictureCreate):
    await post_picture_controller.create_post_picture(obj_in=picture_in)
    return Success(msg="Created Successfully")

@router.delete("/delete", summary="删除帖子图片", description="根据图片ID删除指定的帖子图片记录")
async def delete_post_picture(id: int = Query(..., description="图片ID")):
    await post_picture_controller.delete_post_picture(picture_id=id)
    return Success(msg="Deleted Successfully")
