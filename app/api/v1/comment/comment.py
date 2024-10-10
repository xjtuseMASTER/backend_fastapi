from fastapi import APIRouter, Query
from app.controllers.comment_controller import comment_controller
from app.schemas import Success
from app.schemas.comment_schemas import CommentCreate, CommentUpdate

router = APIRouter()

@router.get("/list", summary="查看评论列表")
async def list_comments(content: str = Query(None, description="评论内容")):
    comments = await comment_controller.get_comments_by_content(content)
    return Success(data=comments)

@router.get("/get", summary="查看评论")
async def get_comment(id: int = Query(..., description="评论ID")):
    comment = await comment_controller.get(id=id)
    return Success(data=comment)

@router.post("/create", summary="创建评论")
async def create_comment(comment_in: CommentCreate):
    await comment_controller.create_comment(obj_in=comment_in)
    return Success(msg="Created Successfully")

@router.post("/update", summary="更新评论")
async def update_comment(comment_in: CommentUpdate):
    await comment_controller.update_comment(obj_in=comment_in)
    return Success(msg="Updated Successfully")

@router.delete("/delete", summary="删除评论")
async def delete_comment(id: int = Query(..., description="评论ID")):
    await comment_controller.delete_comment(comment_id=id)
    return Success(msg="Deleted Successfully")
