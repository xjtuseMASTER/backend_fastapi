from fastapi import APIRouter

from .post_picture import router

post_picture_router = APIRouter()
post_picture_router.include_router(router, tags=["帖子图片模块"])

__all__ = ["post_picture_router"]
