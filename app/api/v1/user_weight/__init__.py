from fastapi import APIRouter

from .user_weight import router

user_weight_router = APIRouter()
user_weight_router.include_router(router, tags=["用户体重历史数据"])

__all__ = ["user_weight_router"]