from fastapi import APIRouter

from .post_like import router

post_like_router = APIRouter()
post_like_router.include_router(router, tags=["帖子的点赞模块"])

__all__ = ["post_like_router"]
