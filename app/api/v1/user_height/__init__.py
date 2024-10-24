from fastapi import APIRouter

from .user_height import router

user_height_router = APIRouter()
user_height_router.include_router(router, tags=["用户身高历史数据"])

__all__ = ["user_height_router"]

