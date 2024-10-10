from fastapi import APIRouter

from .comment_like import router

comment_like_router = APIRouter()
comment_like_router.include_router(router, tags=["评论的点赞模块"])

__all__ = ["comment_like_router"]
