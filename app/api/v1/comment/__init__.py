from fastapi import APIRouter

from .comment import router

comment_router = APIRouter()
comment_router.include_router(router, tags=["菜单模块"])

__all__ = ["comment_router"]
