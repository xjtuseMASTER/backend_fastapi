from tortoise import fields


from .base import BaseModel, TimestampMixin
from .enums import MethodType



class User(BaseModel, TimestampMixin):
    """
    用户模型：用于存储用户的基本信息。
    """
    user_id = fields.CharField(pk=True, max_length=36, description="用户ID", index=True)
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
    be_followed_num = fields.IntField(default=0, description="被关注数量", index=True)
    be_liked_num = fields.IntField(default=0, description="所有帖子被点赞数量", index=True)
    be_collected_num = fields.IntField(default=0, description="所有帖子被收藏数量", index=True)

    class Meta:
        table = "t_user"
        table_description = "用户表：存储用户的基本信息及相关数据"

class Post(BaseModel, TimestampMixin):
    """
    帖子模型：用于存储用户发布的帖子内容
    """
    post_id = fields.CharField(pk=True, max_length=36, description="帖子ID", index=True)  # Changed from IntField to CharField (UUID)
    user_id = fields.ForeignKeyField("models.User", related_name="posts", description="用户ID")  # Foreign key changed to CharField
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
    comment_id = fields.CharField(pk=True, max_length=36, description="评论ID", index=True)  # Changed from IntField to CharField (UUID)
    post_id = fields.ForeignKeyField("models.Post", related_name="comments", description="关联帖子ID")  # Foreign key changed to CharField
    user_id = fields.ForeignKeyField("models.User", related_name="comments", description="用户ID")  # Foreign key changed to CharField
    father_comment_id = fields.CharField("",max_length=36, description="评论ID", index=True)
    content = fields.TextField(description="评论内容")
    level = fields.IntField(description="评论层级", index=True)
    likes_num = fields.IntField(default=0, description="点赞数量")
    
    class Meta:
        table = "t_comment"
        table_description = "评论表，用于存储帖子的评论数据"

# 关注模型
class Follower(BaseModel, TimestampMixin):
    follower_id = fields.CharField(pk=True, max_length=36, description="关注者ID", index=True)  # Changed to CharField (UUID)
    to_user_id = fields.ForeignKeyField("models.User", related_name="followers", description="被关注用户ID")  # ForeignKey to User
    follow_each_other = fields.IntnField(default=0, description="是否互相关注")

    class Meta:
        table = "t_followers"
        table_description = "关注表，存储用户之间的关注关系"

# 帖子点赞模型
class PostLike(BaseModel, TimestampMixin):
    like_id = fields.CharField(pk=True, max_length=36, description="点赞ID", index=True)  # Changed to CharField (UUID)
    user_id = fields.ForeignKeyField("models.User", related_name="post_likes", description="点赞用户ID")  # ForeignKey to User
    to_post_id = fields.ForeignKeyField("models.Post", related_name="likes", description="关联帖子ID")  # ForeignKey to Post

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
    collect_id = fields.CharField(pk=True, max_length=36, description="收藏ID", index=True)  # Changed to CharField (UUID)
    user_id = fields.ForeignKeyField("models.User", related_name="post_collects", description="收藏用户ID")  # ForeignKey to User
    to_post_id = fields.ForeignKeyField("models.Post", related_name="collects", description="关联帖子ID")  # ForeignKey to Post

    create_time = fields.DatetimeField(auto_now_add=True, description="收藏时间")

    class Meta:
        table = "t_post_collects"
        table_description = "帖子收藏表"

# 帖子图片模型
class PostPicture(BaseModel, TimestampMixin):
    pictures_id = fields.CharField(pk=True, max_length=36, description="图片ID", index=True)  # Changed to CharField (UUID)
    to_post_id = fields.ForeignKeyField("models.Post", related_name="pictures", description="关联帖子ID")  # ForeignKey to Post
    sequence = fields.IntField(description="图片顺序")
    position = fields.CharField(max_length=255, description="图片位置")

    class Meta:
        table = "t_post_pictures"
        table_description = "帖子图片表"


class UserPreference(BaseModel):
    user_id = fields.ForeignKeyField("models.User", related_name="preferences", description="用户ID")
    app_notification = fields.BooleanField(default=True, description="是否开启消息提醒")
    theme = fields.CharField(max_length=50, description="主题", default="light")

    class Meta:
        table = "t_user_preference"
        table_description = "用户偏好设置表"

class HistoryUploads(BaseModel):
    user_id = fields.ForeignKeyField("models.User", related_name="history_uploads", description="用户ID")
    video_url = fields.CharField(max_length=255, description="视频URL")
    analysis = fields.TextField(description="分析记录")

    class Meta:
        table = "t_history_uploads"
        table_description = "历史健身上传记录表"
        
        
class BodyData(BaseModel, TimestampMixin):
    user_id = fields.ForeignKeyField("models.User", related_name="body_data", description="用户ID", pk=True)  # ForeignKey to User
    height = fields.FloatField(description="身高")
    weight = fields.FloatField(description="体重")
    lung_capacity = fields.FloatField(description="肺活量")
    bmi = fields.FloatField(description="BMI")

    class Meta:
        table = "t_body_data"
        table_description = "用户身体数据表"
        
        
class Muscle(BaseModel, TimestampMixin):
    user_id = fields.ForeignKeyField("models.User", related_name="muscles", description="用户ID")  # ForeignKey to User
    muscle_id = fields.CharField(max_length=36, description="肌肉ID", index=True)  # CharField for UUID
    muscle_name = fields.CharField(max_length=255, description="肌肉名称")
    muscle_description = fields.TextField(description="肌肉描述")

    class Meta:
        table = "t_muscle"
        table_description = "用户肌肉数据表"
        unique_together = ("user_id", "muscle_id")  # Composite primary key using user_id and muscle_id
