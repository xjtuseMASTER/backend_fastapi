from fastapi import APIRouter

from app.core.dependency import DependPermisson

from .apis import apis_router
# from .auditlog import auditlog_router
# from .base import base_router
# from .depts import depts_router
# from .menus import menus_router
from .user import user_router
from .follower import follower_router
from .post import post_router
from .comment import comment_router
from .post_like import post_like_router







v1_router = APIRouter()

# v1_router.include_router(base_router, prefix="/base")

# v1_router.include_router(menus_router, prefix="/menu", dependencies=[DependPermisson])
v1_router.include_router(apis_router, prefix="/api", dependencies=[DependPermisson])
# v1_router.include_router(depts_router, prefix="/dept", dependencies=[DependPermisson])
# v1_router.include_router(auditlog_router, prefix="/auditlog", dependencies=[DependPermisson])


v1_router.include_router(user_router, prefix="/user", dependencies=[DependPermisson])
v1_router.include_router(post_router, prefix="/post", dependencies=[DependPermisson])
v1_router.include_router(follower_router, prefix="/follower", dependencies=[DependPermisson])
v1_router.include_router(comment_router, prefix="/comment", dependencies=[DependPermisson])
v1_router.include_router(post_like_router, prefix="/post_like", dependencies=[DependPermisson])
