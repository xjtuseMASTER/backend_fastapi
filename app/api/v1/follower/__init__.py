from fastapi import APIRouter

from .follower import router

follower_router = APIRouter()
follower_router.include_router(router, tags=["关注模块"])

__all__ = ["follower_router"]
