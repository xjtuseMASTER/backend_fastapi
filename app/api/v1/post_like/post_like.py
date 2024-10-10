import logging
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.post import PostLike
from app.schemas.post_like_schemas import PostLikeCreate, PostLikeUpdate, BasePostLike

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/", response_model=BasePostLike, summary="创建帖子点赞", description="根据提供的信息创建一个新的帖子点赞记录")
async def create_post_like(post_like: PostLikeCreate):
    new_like = await PostLike.create(**post_like.dict())
    return new_like

@router.get("/", response_model=List[BasePostLike], summary="获取所有帖子点赞", description="返回数据库中所有帖子的点赞记录")
async def get_all_post_likes():
    return await PostLike.all()
