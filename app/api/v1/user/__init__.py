from fastapi import APIRouter

from .user import router

user_router = APIRouter()
user_router.include_router(router, tags=["用户模块"])

__all__ = ["user_router"]
