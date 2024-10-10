from fastapi import APIRouter, Query
from app.controllers.comment_like_controller import comment_like_controller
from app.schemas import Success
from app.schemas.comment_like_schemas import CommentLikeCreate

router = APIRouter()

@router.post("/create", summary="创建评论点赞", description="根据提供的信息创建一个新的评论点赞记录")
async def create_comment_like(like_in: CommentLikeCreate):
    await comment_like_controller.create_comment_like(obj_in=like_in)
    return Success(msg="Created Successfully")

@router.delete("/delete", summary="删除评论点赞", description="根据点赞ID删除指定的评论点赞记录")
async def delete_comment_like(id: int = Query(..., description="评论点赞ID")):
    await comment_like_controller.delete_comment_like(like_id=id)
    return Success(msg="Deleted Successfully")
