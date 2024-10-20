from tortoise import fields


from .base import BaseModel, TimestampMixin
from .enums import MethodType



class User(BaseModel, TimestampMixin):
    """
    用户模型：用于存储用户的基本信息。
    """
    user_id = fields.CharField(pk=True, max_length=36, description="用户ID")
    email = fields.CharField(max_length=255, unique=True, description="用户邮箱")
    password = fields.CharField(max_length=255, description="用户密码")
    likes_num = fields.IntField(default=0, description="点赞数量")
    user_name = fields.CharField(max_length=255, description="用户名")
    birthday = fields.DateField(null=True, description="用户生日")
    selfIntro = fields.CharField(max_length=255, null=True, description="自我介绍")
    avatar = fields.CharField(max_length=255, null=True, description="用户头像链接")
    gender = fields.CharField(max_length=50, null=True, description="用户性别")
    followers_num = fields.IntField(default=0, description="关注数")
    collects_num = fields.IntField(default=0, description="收藏数")
    be_followed_num = fields.IntField(default=0, description="被关注数量")
    be_liked_num = fields.IntField(default=0, description="所有帖子被点赞数量")
    be_collected_num = fields.IntField(default=0, description="所有帖子被收藏数量")

    class Meta:
        table = "t_user"
        table_description = "用户表：存储用户的基本信息及相关数据"

class Post(BaseModel, TimestampMixin):
    """
    帖子模型：用于存储用户发布的帖子内容
    """
    post_id = fields.CharField(pk=True, max_length=36, description="帖子ID")  # Changed from IntField to CharField (UUID)
    user_id = fields.CharField(max_length=36, description="用户ID")  # Foreign key changed to CharField
    title = fields.CharField(max_length=255, description="帖子标题")
    content = fields.TextField(description="帖子内容")
    create_time = fields.DatetimeField(auto_now_add=True, description="创建时间")
    update_time = fields.DatetimeField(auto_now=True, description="更新时间")
    likes_num = fields.IntField(default=0, description="点赞数量")
    collects_num = fields.IntField(default=0, description="收藏数量")
    comments_num = fields.IntField(default=0, description="评论数量")

    class Meta:
        table = "t_post"
        table_description = "帖子表，用于存储用户发布的帖子内容"

# 评论模型
class Comment(BaseModel, TimestampMixin):
    comment_id = fields.CharField(pk=True, max_length=36, description="评论ID")  # Changed from IntField to CharField (UUID)
    post_id = fields.CharField(max_length=36, description="关联帖子ID")  # Foreign key changed to CharField
    user_id = fields.CharField(max_length=36, description="用户ID")  # Foreign key changed to CharField
    father_comment_id = fields.CharField(max_length=36, description="评论ID")
    content = fields.TextField(description="评论内容")
    level = fields.IntField(description="评论层级")
    likes_num = fields.IntField(default=0, description="点赞数量")
    
    class Meta:
        table = "t_comment"
        table_description = "评论表，用于存储帖子的评论数据"

# 关注模型
class Follower(BaseModel, TimestampMixin):
    follower_id = fields.CharField(pk=True, max_length=36, description="关注者ID")  # Changed to CharField (UUID)
    to_user_id = fields.CharField(max_length=36, description="被关注用户ID")  # ForeignKey to User
    follow_each_other = fields.IntField(default=0, description="是否互相关注")

    class Meta:
        table = "t_followers"
        table_description = "关注表，存储用户之间的关注关系"

# 帖子点赞模型
class PostLike(BaseModel, TimestampMixin):
    like_id = fields.CharField(pk=True, max_length=36, description="点赞ID")  # Changed to CharField (UUID)
    user_id = fields.CharField(max_length=36, description="点赞用户ID")  # ForeignKey to User
    to_post_id = fields.CharField(max_length=36, description="关联帖子ID")  # ForeignKey to Post

    create_time = fields.DatetimeField(auto_now_add=True, description="点赞时间")

    class Meta:
        table = "t_post_likes"
        table_description = "帖子点赞表"

# 评论点赞模型
class CommentLike(BaseModel, TimestampMixin):
    like_id = fields.IntField(pk=True, description="点赞ID")
    user_id = fields.IntField(description="点赞用户ID")
    to_comment_id = fields.IntField(description="关联评论ID")
    create_time = fields.DatetimeField(auto_now_add=True, description="点赞时间")

    class Meta:
        table = "t_comment_likes"
        table_description = "评论点赞表"

# 帖子收藏模型
class PostCollect(BaseModel, TimestampMixin):
    collect_id = fields.CharField(pk=True, max_length=36, description="收藏ID")  # Changed to CharField (UUID)
    user_id = fields.CharField(max_length=36, description="收藏用户ID")  # ForeignKey to User
    to_post_id = fields.CharField(max_length=36, description="关联帖子ID")  # ForeignKey to Post

    create_time = fields.DatetimeField(auto_now_add=True, description="收藏时间")

    class Meta:
        table = "t_post_collects"
        table_description = "帖子收藏表"

# 帖子图片模型
class PostPicture(BaseModel, TimestampMixin):
    pictures_id = fields.CharField(pk=True, max_length=36, description="图片ID")  # Changed to CharField (UUID)
    to_post_id = fields.CharField(max_length=36, description="关联帖子ID")  # ForeignKey to Post
    sequence = fields.IntField(description="图片顺序")
    position = fields.CharField(max_length=255, description="图片位置")

    class Meta:
        table = "t_post_pictures"
        table_description = "帖子图片表"


class UserPreference(BaseModel):
    user_id = fields.CharField(max_length=36, description="用户ID",pk=True)
    app_notification = fields.BooleanField(default=True, description="是否开启消息提醒")
    theme = fields.CharField(max_length=50, description="主题", default="light")

    class Meta:
        table = "t_user_preference"
        table_description = "用户偏好设置表"

class HistoryUploads(BaseModel):
    user_id = fields.CharField(max_length=36, description="用户ID",pk=True)
    video_url = fields.CharField(max_length=255, description="视频URL")
    analysis = fields.TextField(description="分析记录")

    class Meta:
        table = "t_history_uploads"
        table_description = "历史健身上传记录表"
        
        
class Muscle(BaseModel, TimestampMixin):
    muscle_id = fields.CharField(pk=True, max_length=36, description="肌肉ID")  # Use muscle_id as the primary key
    user_id = fields.CharField(max_length=36, description="用户ID")  # ForeignKey, not primary key
    muscle_name = fields.CharField(max_length=255, description="肌肉名称")
    muscle_description = fields.TextField(description="肌肉描述")

    class Meta:
        table = "t_muscle"
        table_description = "用户肌肉数据表"
        unique_together = ("user_id", "muscle_id")  # Ensure unique combination of user_id and muscle_id
        
        
        
class UserFeedback(BaseModel, TimestampMixin):
    user_id = fields.CharField(pk=True,max_length=36, description="用户ID")
    feedback_text = fields.TextField(description="反馈内容")
    created_at = fields.DatetimeField(auto_now_add=True, description="创建时间")

    class Meta:
        table = "t_user_feedback"
        table_description = "用户反馈表"


class UserHeight(BaseModel, TimestampMixin):
    user_id = fields.CharField(pk=True,max_length=36, description="用户ID")
    height = fields.FloatField(description="身高 (cm)")
    record_date = fields.DateField(description="记录日期")

    class Meta:
        table = "t_user_height"
        table_description = "用户身高数据表"
        unique_together = ("user_id", "record_date")



class UserHeight(BaseModel, TimestampMixin):
    user_id = fields.CharField(pk=True,max_length=36, description="用户ID")
    height = fields.FloatField(description="身高 (cm)")
    record_date = fields.DateField(description="记录日期")

    class Meta:
        table = "t_user_height"
        table_description = "用户身高数据表"
        unique_together = ("user_id", "record_date")




class UserVitalCapacity(BaseModel, TimestampMixin):
    user_id = fields.CharField(pk=True,max_length=36, description="用户ID")
    vital_capacity = fields.FloatField(description="肺活量 (mL)")
    record_date = fields.DateField(description="记录日期")

    class Meta:
        table = "t_user_vital_capacity"
        table_description = "用户肺活量数据表"
        unique_together = ("user_id", "record_date")



class UserBodyFatRate(BaseModel, TimestampMixin):
    user_id = fields.CharField(pk=True,max_length=36, description="用户ID")
    body_fat_rate = fields.FloatField(description="体脂率 (%)")
    record_date = fields.DateField(description="记录日期")

    class Meta:
        table = "t_user_body_fat_rate"
        table_description = "用户体脂率数据表"
        unique_together = ("user_id", "record_date")
