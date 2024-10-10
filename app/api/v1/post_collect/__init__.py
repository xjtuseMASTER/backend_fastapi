from fastapi import APIRouter

from .post_collect import router

post_collect_router = APIRouter()
post_collect_router.include_router(router, tags=["帖子的收藏模块"])

__all__ = ["post_collect_router"]
