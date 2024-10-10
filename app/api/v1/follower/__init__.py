from fastapi import APIRouter

from .follower import router

follower_router = APIRouter()
follower_router.include_router(router, tags=["菜单模块"])

__all__ = ["follower_router"]
