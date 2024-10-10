from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        CREATE TABLE IF NOT EXISTS `t_comment` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `comment_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '评论ID',
    `post_id` INT NOT NULL  COMMENT '关联帖子ID',
    `user_id` INT NOT NULL  COMMENT '用户ID',
    `father_comment_id` INT   COMMENT '父评论ID',
    `content` LONGTEXT NOT NULL  COMMENT '评论内容',
    `level` INT NOT NULL  COMMENT '评论层级',
    `likes_num` INT NOT NULL  COMMENT '点赞数量' DEFAULT 0,
    KEY `idx_t_comment_id_1e66f9` (`id`),
    KEY `idx_t_comment_created_7ab37f` (`created_at`),
    KEY `idx_t_comment_updated_e71593` (`updated_at`),
    KEY `idx_t_comment_post_id_9a5dc0` (`post_id`),
    KEY `idx_t_comment_user_id_4d0e7c` (`user_id`),
    KEY `idx_t_comment_father__28475f` (`father_comment_id`),
    KEY `idx_t_comment_level_878f0c` (`level`)
) CHARACTER SET utf8mb4 COMMENT='评论表，用于存储帖子的评论数据';
CREATE TABLE IF NOT EXISTS `t_comment_likes` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `like_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '点赞ID',
    `user_id` INT NOT NULL  COMMENT '点赞用户ID',
    `to_comment_id` INT NOT NULL  COMMENT '关联评论ID',
    `create_time` DATETIME(6) NOT NULL  COMMENT '点赞时间' DEFAULT CURRENT_TIMESTAMP(6),
    KEY `idx_t_comment_l_id_753432` (`id`),
    KEY `idx_t_comment_l_created_642fc3` (`created_at`),
    KEY `idx_t_comment_l_updated_a339e7` (`updated_at`),
    KEY `idx_t_comment_l_user_id_be50a5` (`user_id`),
    KEY `idx_t_comment_l_to_comm_1b0eb8` (`to_comment_id`)
) CHARACTER SET utf8mb4 COMMENT='评论点赞表';
CREATE TABLE IF NOT EXISTS `t_followers` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `follower_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '关注者ID',
    `to_user_id` INT NOT NULL  COMMENT '被关注用户ID',
    `follow_each_other` BOOL NOT NULL  COMMENT '是否互相关注' DEFAULT 0,
    KEY `idx_t_followers_id_77d93d` (`id`),
    KEY `idx_t_followers_created_952c96` (`created_at`),
    KEY `idx_t_followers_updated_9f9a65` (`updated_at`),
    KEY `idx_t_followers_to_user_98db2c` (`to_user_id`)
) CHARACTER SET utf8mb4 COMMENT='关注表，存储用户之间的关注关系';
CREATE TABLE IF NOT EXISTS `t_post` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `post_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '帖子ID',
    `user_id` INT NOT NULL  COMMENT '用户ID',
    `title` VARCHAR(255) NOT NULL  COMMENT '帖子标题',
    `content` LONGTEXT NOT NULL  COMMENT '帖子内容',
    `create_time` DATETIME(6) NOT NULL  COMMENT '创建时间' DEFAULT CURRENT_TIMESTAMP(6),
    `update_time` DATETIME(6) NOT NULL  COMMENT '更新时间' DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `likes_num` INT NOT NULL  COMMENT '点赞数量' DEFAULT 0,
    `collects_num` INT NOT NULL  COMMENT '收藏数量' DEFAULT 0,
    `comments_num` INT NOT NULL  COMMENT '评论数量' DEFAULT 0,
    KEY `idx_t_post_id_90e64a` (`id`),
    KEY `idx_t_post_created_19a018` (`created_at`),
    KEY `idx_t_post_updated_ff8418` (`updated_at`),
    KEY `idx_t_post_user_id_4371c2` (`user_id`),
    KEY `idx_t_post_title_3c14af` (`title`),
    KEY `idx_t_post_likes_n_d79510` (`likes_num`),
    KEY `idx_t_post_collect_51e9d7` (`collects_num`),
    KEY `idx_t_post_comment_4e0475` (`comments_num`)
) CHARACTER SET utf8mb4 COMMENT='帖子表，用于存储用户发布的帖子内容';
CREATE TABLE IF NOT EXISTS `t_post_collects` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `collect_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '收藏ID',
    `user_id` INT NOT NULL  COMMENT '收藏用户ID',
    `to_post_id` INT NOT NULL  COMMENT '关联帖子ID',
    `create_time` DATETIME(6) NOT NULL  COMMENT '收藏时间' DEFAULT CURRENT_TIMESTAMP(6),
    KEY `idx_t_post_coll_id_1ad532` (`id`),
    KEY `idx_t_post_coll_created_3c5621` (`created_at`),
    KEY `idx_t_post_coll_updated_d6b869` (`updated_at`),
    KEY `idx_t_post_coll_user_id_226456` (`user_id`),
    KEY `idx_t_post_coll_to_post_766834` (`to_post_id`)
) CHARACTER SET utf8mb4 COMMENT='帖子收藏表';
CREATE TABLE IF NOT EXISTS `t_post_likes` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `like_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '点赞ID',
    `user_id` INT NOT NULL  COMMENT '点赞用户ID',
    `to_post_id` INT NOT NULL  COMMENT '关联帖子ID',
    `create_time` DATETIME(6) NOT NULL  COMMENT '点赞时间' DEFAULT CURRENT_TIMESTAMP(6),
    KEY `idx_t_post_like_id_594f11` (`id`),
    KEY `idx_t_post_like_created_2785fe` (`created_at`),
    KEY `idx_t_post_like_updated_3785f1` (`updated_at`),
    KEY `idx_t_post_like_user_id_fc56df` (`user_id`),
    KEY `idx_t_post_like_to_post_936fb7` (`to_post_id`)
) CHARACTER SET utf8mb4 COMMENT='帖子点赞表';
CREATE TABLE IF NOT EXISTS `t_post_pictures` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `pictures_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '图片ID',
    `to_post_id` INT NOT NULL  COMMENT '关联帖子ID',
    `sequence` INT NOT NULL  COMMENT '图片顺序',
    `position` VARCHAR(255) NOT NULL  COMMENT '图片位置',
    KEY `idx_t_post_pict_id_5b6fd1` (`id`),
    KEY `idx_t_post_pict_created_c00986` (`created_at`),
    KEY `idx_t_post_pict_updated_cb0718` (`updated_at`),
    KEY `idx_t_post_pict_to_post_6931d6` (`to_post_id`)
) CHARACTER SET utf8mb4 COMMENT='帖子图片表';
CREATE TABLE IF NOT EXISTS `t_user` (
    `id` BIGINT NOT NULL,
    `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6),
    `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6),
    `user_id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT COMMENT '用户ID',
    `email` VARCHAR(255) NOT NULL UNIQUE COMMENT '用户邮箱',
    `password` VARCHAR(255) NOT NULL  COMMENT '用户密码',
    `likes_num` INT NOT NULL  COMMENT '点赞数量' DEFAULT 0,
    `user_name` VARCHAR(255) NOT NULL  COMMENT '用户名',
    `birthday` DATE   COMMENT '用户生日',
    `selfIntro` VARCHAR(255)   COMMENT '自我介绍',
    `avatar` VARCHAR(255)   COMMENT '用户头像链接',
    `gender` VARCHAR(50)   COMMENT '用户性别',
    `followers_num` INT NOT NULL  COMMENT '关注数' DEFAULT 0,
    `collects_num` INT NOT NULL  COMMENT '收藏数' DEFAULT 0,
    KEY `idx_t_user_id_49a745` (`id`),
    KEY `idx_t_user_created_9700b0` (`created_at`),
    KEY `idx_t_user_updated_ade55c` (`updated_at`),
    KEY `idx_t_user_email_6fe6a5` (`email`),
    KEY `idx_t_user_likes_n_2429fe` (`likes_num`),
    KEY `idx_t_user_user_na_33a344` (`user_name`),
    KEY `idx_t_user_gender_778006` (`gender`),
    KEY `idx_t_user_followe_2bf6fe` (`followers_num`),
    KEY `idx_t_user_collect_9bbcd8` (`collects_num`)
) CHARACTER SET utf8mb4 COMMENT='用户表：存储用户的基本信息及相关数据';
CREATE TABLE IF NOT EXISTS `aerich` (
    `id` INT NOT NULL PRIMARY KEY AUTO_INCREMENT,
    `version` VARCHAR(255) NOT NULL,
    `app` VARCHAR(100) NOT NULL,
    `content` JSON NOT NULL
) CHARACTER SET utf8mb4;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        """
