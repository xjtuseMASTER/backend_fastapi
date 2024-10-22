from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `t_comment` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `comment_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '评论ID',
    `post_id` VARCHAR(36) NOT NULL  COMMENT '关联帖子ID',
    `user_id` VARCHAR(36) NOT NULL  COMMENT '用户ID',
    `father_comment_id` VARCHAR(36) NOT NULL  COMMENT '评论ID',
    `content` LONGTEXT NOT NULL  COMMENT '评论内容',
    `level` INT NOT NULL  COMMENT '评论层级',
    `likes_num` INT NOT NULL  COMMENT '点赞数量' DEFAULT 0
) CHARACTER SET utf8mb4 COMMENT='评论表，用于存储帖子的评论数据';
CREATE TABLE IF NOT EXISTS `t_comment_likes` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `like_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '点赞ID',
    `user_id` INT NOT NULL  COMMENT '点赞用户ID',
    `to_comment_id` INT NOT NULL  COMMENT '关联评论ID',
    `create_time` DATETIME(6) NOT NULL  COMMENT '点赞时间' DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4 COMMENT='评论点赞表';
CREATE TABLE IF NOT EXISTS `t_followers` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `follower_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '关注者ID',
    `to_user_id` VARCHAR(36) NOT NULL  COMMENT '被关注用户ID',
    `follow_each_other` INT NOT NULL  COMMENT '是否互相关注' DEFAULT 0
) CHARACTER SET utf8mb4 COMMENT='关注表，存储用户之间的关注关系';
CREATE TABLE IF NOT EXISTS `t_history_uploads` (
    `id` BIGINT NOT NULL,
    `user_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '用户ID',
    `video_url` VARCHAR(255) NOT NULL  COMMENT '视频URL',
    `analysis` LONGTEXT NOT NULL  COMMENT '分析记录'
) CHARACTER SET utf8mb4 COMMENT='历史健身上传记录表';
CREATE TABLE IF NOT EXISTS `t_muscle` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `muscle_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '肌肉ID',
    `user_id` VARCHAR(36) NOT NULL  COMMENT '用户ID',
    `muscle_name` VARCHAR(255) NOT NULL  COMMENT '肌肉名称',
    `muscle_description` LONGTEXT NOT NULL  COMMENT '肌肉描述',
    UNIQUE KEY `uid_t_muscle_user_id_cd0779` (`user_id`, `muscle_id`)
) CHARACTER SET utf8mb4 COMMENT='用户肌肉数据表';
CREATE TABLE IF NOT EXISTS `t_post` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `post_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '帖子ID',
    `user_id` VARCHAR(36) NOT NULL  COMMENT '用户ID',
    `title` VARCHAR(255) NOT NULL  COMMENT '帖子标题',
    `content` LONGTEXT NOT NULL  COMMENT '帖子内容',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `likes_num` INT NOT NULL  COMMENT '点赞数量' DEFAULT 0,
    `collects_num` INT NOT NULL  COMMENT '收藏数量' DEFAULT 0,
    `comments_num` INT NOT NULL  COMMENT '评论数量' DEFAULT 0
) CHARACTER SET utf8mb4 COMMENT='帖子表，用于存储用户发布的帖子内容';
CREATE TABLE IF NOT EXISTS `t_post_collects` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `collect_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '收藏ID',
    `user_id` VARCHAR(36) NOT NULL  COMMENT '收藏用户ID',
    `to_post_id` VARCHAR(36) NOT NULL  COMMENT '关联帖子ID',
    `create_time` DATETIME(6) NOT NULL  COMMENT '收藏时间' DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4 COMMENT='帖子收藏表';
CREATE TABLE IF NOT EXISTS `t_post_likes` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `like_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '点赞ID',
    `user_id` VARCHAR(36) NOT NULL  COMMENT '点赞用户ID',
    `to_post_id` VARCHAR(36) NOT NULL  COMMENT '关联帖子ID',
    `create_time` DATETIME(6) NOT NULL  COMMENT '点赞时间' DEFAULT CURRENT_TIMESTAMP(6)
) CHARACTER SET utf8mb4 COMMENT='帖子点赞表';
CREATE TABLE IF NOT EXISTS `t_post_pictures` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `pictures_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '图片ID',
    `to_post_id` VARCHAR(36) NOT NULL  COMMENT '关联帖子ID',
    `sequence` INT NOT NULL  COMMENT '图片顺序',
    `position` VARCHAR(255) NOT NULL  COMMENT '图片位置'
) CHARACTER SET utf8mb4 COMMENT='帖子图片表';
CREATE TABLE IF NOT EXISTS `t_user` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '用户ID',
    `email` VARCHAR(255) NOT NULL UNIQUE COMMENT '用户邮箱',
    `password` VARCHAR(255) NOT NULL  COMMENT '用户密码',
    `likes_num` INT NOT NULL  COMMENT '点赞数量' DEFAULT 0,
    `user_name` VARCHAR(255) NOT NULL  COMMENT '用户名',
    `birthday` DATETIME(6)   COMMENT '用户生日',
    `selfIntro` VARCHAR(255)   COMMENT '自我介绍',
    `avatar` VARCHAR(255)   COMMENT '用户头像链接',
    `gender` VARCHAR(50)   COMMENT '用户性别',
    `followers_num` INT NOT NULL  COMMENT '关注数' DEFAULT 0,
    `collects_num` INT NOT NULL  COMMENT '收藏数' DEFAULT 0,
    `be_followed_num` INT NOT NULL  COMMENT '被关注数量' DEFAULT 0,
    `be_liked_num` INT NOT NULL  COMMENT '所有帖子被点赞数量' DEFAULT 0,
    `be_collected_num` INT NOT NULL  COMMENT '所有帖子被收藏数量' DEFAULT 0
) CHARACTER SET utf8mb4 COMMENT='用户表：存储用户的基本信息及相关数据';
CREATE TABLE IF NOT EXISTS `t_user_body_fat_rate` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '用户ID',
    `body_fat_rate` DOUBLE NOT NULL  COMMENT '体脂率 (%)',
    `record_date` DATE NOT NULL  COMMENT '记录日期',
    UNIQUE KEY `uid_t_user_body_user_id_f6d940` (`user_id`, `record_date`)
) CHARACTER SET utf8mb4 COMMENT='用户体脂率数据表';
CREATE TABLE IF NOT EXISTS `t_user_feedback` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '用户ID',
    `feedback_text` LONGTEXT NOT NULL  COMMENT '反馈内容'
) CHARACTER SET utf8mb4 COMMENT='用户反馈表';
CREATE TABLE IF NOT EXISTS `t_user_height` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '用户ID',
    `height` DOUBLE NOT NULL  COMMENT '身高 (cm)',
    `record_date` DATE NOT NULL  COMMENT '记录日期',
    UNIQUE KEY `uid_t_user_heig_user_id_347269` (`user_id`, `record_date`)
) CHARACTER SET utf8mb4 COMMENT='用户身高数据表';
CREATE TABLE IF NOT EXISTS `t_user_preference` (
    `id` BIGINT NOT NULL,
    `user_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '用户ID',
    `app_notification` BOOL NOT NULL  COMMENT '是否开启消息提醒' DEFAULT 1,
    `theme` VARCHAR(50) NOT NULL  COMMENT '主题' DEFAULT 'light'
) CHARACTER SET utf8mb4 COMMENT='用户偏好设置表';
CREATE TABLE IF NOT EXISTS `t_user_vital_capacity` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `user_id` VARCHAR(36) NOT NULL  PRIMARY KEY COMMENT '用户ID',
    `vital_capacity` DOUBLE NOT NULL  COMMENT '肺活量 (mL)',
    `record_date` DATE NOT NULL  COMMENT '记录日期',
    UNIQUE KEY `uid_t_user_vita_user_id_91f44a` (`user_id`, `record_date`)
) CHARACTER SET utf8mb4 COMMENT='用户肺活量数据表';
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
