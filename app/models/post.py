from tortoise import fields


from .base import BaseModel, TimestampMixin
from .enums import MethodType



class User(BaseModel, TimestampMixin):
    """
    用户模型：用于存储用户的基本信息。
    """
    user_id = fields.IntField(pk=True, description="用户ID", index=True)
    email = fields.CharField(max_length=255, unique=True, description="用户邮箱", index=True)
    password = fields.CharField(max_length=255, description="用户密码")
    likes_num = fields.IntField(default=0, description="点赞数量", index=True)
    user_name = fields.CharField(max_length=255, description="用户名", index=True)
    birthday = fields.DateField(null=True, description="用户生日")
    selfIntro = fields.CharField(max_length=255, null=True, description="自我介绍")
    avatar = fields.CharField(max_length=255, null=True, description="用户头像链接")
    gender = fields.CharField(max_length=50, null=True, description="用户性别", index=True)
    followers_num = fields.IntField(default=0, description="关注数", index=True)
    collects_num = fields.IntField(default=0, description="收藏数", index=True)

    class Meta:
        table = "t_user"
        table_description = "用户表：存储用户的基本信息及相关数据"

class Post(BaseModel, TimestampMixin):
    """
    帖子模型：用于存储用户发布的帖子内容
    """
    post_id = fields.IntField(pk=True, description="帖子ID", index=True)
    user_id = fields.IntField(description="用户ID", index=True)
    title = fields.CharField(max_length=255, description="帖子标题", index=True)
    content = fields.TextField(description="帖子内容")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")
    likes_num = fields.IntField(default=0, description="点赞数量", index=True)
    collects_num = fields.IntField(default=0, description="收藏数量", index=True)
    comments_num = fields.IntField(default=0, description="评论数量", index=True)

    class Meta:
        table = "t_post"
        table_description = "帖子表，用于存储用户发布的帖子内容"

# 评论模型
class Comment(BaseModel, TimestampMixin):
    comment_id = fields.IntField(pk=True, description="评论ID", index=True)
    post_id = fields.IntField(description="关联帖子ID", index=True)
    user_id = fields.IntField(description="用户ID", index=True)
    father_comment_id = fields.IntField(null=True, description="父评论ID", index=True)
    content = fields.TextField(description="评论内容")
    level = fields.IntField(description="评论层级", index=True)
    likes_num = fields.IntField(default=0, description="点赞数量")
    
    class Meta:
        table = "t_comment"
        table_description = "评论表，用于存储帖子的评论数据"

# 关注模型
class Follower(BaseModel, TimestampMixin):
    follower_id = fields.IntField(pk=True, description="关注者ID", index=True)
    to_user_id = fields.IntField(description="被关注用户ID", index=True)
    follow_each_other = fields.BooleanField(default=False, description="是否互相关注")

    class Meta:
        table = "t_followers"
        table_description = "关注表，存储用户之间的关注关系"

# 帖子点赞模型
class PostLike(BaseModel, TimestampMixin):
    like_id = fields.IntField(pk=True, description="点赞ID", index=True)
    user_id = fields.IntField(description="点赞用户ID", index=True)
    to_post_id = fields.IntField(description="关联帖子ID", index=True)
    create_time = fields.DatetimeField(auto_now_add=True, description="点赞时间")

    class Meta:
        table = "t_post_likes"
        table_description = "帖子点赞表"

# 评论点赞模型
class CommentLike(BaseModel, TimestampMixin):
    like_id = fields.IntField(pk=True, description="点赞ID", index=True)
    user_id = fields.IntField(description="点赞用户ID", index=True)
    to_comment_id = fields.IntField(description="关联评论ID", index=True)
    create_time = fields.DatetimeField(auto_now_add=True, description="点赞时间")

    class Meta:
        table = "t_comment_likes"
        table_description = "评论点赞表"

# 帖子收藏模型
class PostCollect(BaseModel, TimestampMixin):
    collect_id = fields.IntField(pk=True, description="收藏ID", index=True)
    user_id = fields.IntField(description="收藏用户ID", index=True)
    to_post_id = fields.IntField(description="关联帖子ID", index=True)
    create_time = fields.DatetimeField(auto_now_add=True, description="收藏时间")

    class Meta:
        table = "t_post_collects"
        table_description = "帖子收藏表"

# 帖子图片模型
class PostPicture(BaseModel, TimestampMixin):
    pictures_id = fields.IntField(pk=True, description="图片ID", index=True)
    to_post_id = fields.IntField(description="关联帖子ID", index=True)
    sequence = fields.IntField(description="图片顺序")
    position = fields.CharField(max_length=255, description="图片位置")

    class Meta:
        table = "t_post_pictures"
        table_description = "帖子图片表"
