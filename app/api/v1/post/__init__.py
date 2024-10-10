from fastapi import APIRouter

from .post import router

post_router = APIRouter()
post_router.include_router(router, tags=["帖子模块"])

__all__ = ["post_router"]
