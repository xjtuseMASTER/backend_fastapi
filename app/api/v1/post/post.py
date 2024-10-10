import logging
from fastapi import APIRouter, HTTPException
from typing import List
from app.models.post import Post
from app.schemas.post_schemas import PostCreate, PostUpdate, BasePost

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/", response_model=BasePost, summary="创建帖子", description="根据提供的帖子信息创建一个新的帖子")
async def create_post(post: PostCreate):
    new_post = await Post.create(**post.dict())
    return new_post

@router.get("/", response_model=List[BasePost], summary="获取所有帖子", description="返回数据库中所有帖子的基本信息")
async def get_all_posts():
    return await Post.all()

@router.get("/{post_id}", response_model=BasePost, summary="获取指定帖子", description="根据帖子ID获取特定帖子信息")
async def get_post_by_id(post_id: int):
    post = await Post.get_or_none(post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    return post

@router.put("/{post_id}", response_model=BasePost, summary="更新帖子信息", description="根据帖子ID更新帖子的基本信息")
async def update_post(post_id: int, post_data: PostUpdate):
    post = await Post.get_or_none(post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    post.update_from_dict(post_data.dict(exclude_unset=True))
    await post.save()
    return post

@router.delete("/{post_id}", response_model=dict, summary="删除帖子", description="根据帖子ID删除帖子信息")
async def delete_post(post_id: int):
    post = await Post.get_or_none(post_id=post_id)
    if not post:
        raise HTTPException(status_code=404, detail="Post not found")
    await post.delete()
    return {"message": "Post deleted successfully"}
