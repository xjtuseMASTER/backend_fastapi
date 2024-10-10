import logging
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.post import Comment
from app.schemas.comment_schemas import CommentCreate, CommentUpdate, BaseComment

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/", response_model=BaseComment, summary="创建评论", description="根据提供的评论信息创建一个新的评论")
async def create_comment(comment: CommentCreate):
    new_comment = await Comment.create(**comment.dict())
    return new_comment

@router.get("/", response_model=List[BaseComment], summary="获取所有评论", description="返回数据库中所有评论的信息")
async def get_all_comments():
    return await Comment.all()

@router.get("/{comment_id}", response_model=BaseComment, summary="获取指定评论", description="根据评论ID获取特定评论信息")
async def get_comment_by_id(comment_id: int):
    comment = await Comment.get_or_none(comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment

@router.put("/{comment_id}", response_model=BaseComment, summary="更新评论信息", description="根据评论ID更新评论的基本信息")
async def update_comment(comment_id: int, comment_data: CommentUpdate):
    comment = await Comment.get_or_none(comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    comment.update_from_dict(comment_data.dict(exclude_unset=True))
    await comment.save()
    return comment

@router.delete("/{comment_id}", response_model=dict, summary="删除评论", description="根据评论ID删除评论信息")
async def delete_comment(comment_id: int):
    comment = await Comment.get_or_none(comment_id=comment_id)
    if not comment:
        raise HTTPException(status_code=404, detail="Comment not found")
    await comment.delete()
    return {"message": "Comment deleted successfully"}
