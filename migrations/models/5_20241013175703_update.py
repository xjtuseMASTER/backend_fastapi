from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `t_body_data` ADD `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_body_data` ADD `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_body_data` ADD `id` BIGINT NOT NULL;
        ALTER TABLE `t_comment` ADD `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_comment` ADD `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_comment` ADD `id` BIGINT NOT NULL;
        ALTER TABLE `t_comment_likes` ADD `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_comment_likes` ADD `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_comment_likes` ADD `id` BIGINT NOT NULL;
        ALTER TABLE `t_followers` ADD `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_followers` ADD `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_followers` ADD `id` BIGINT NOT NULL;
        ALTER TABLE `t_history_uploads` ADD `id` BIGINT NOT NULL;
        ALTER TABLE `t_muscle` ADD `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_muscle` ADD `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_muscle` ADD `id` BIGINT NOT NULL;
        ALTER TABLE `t_post` ADD `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_post` ADD `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_post` ADD `id` BIGINT NOT NULL;
        ALTER TABLE `t_post_collects` ADD `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_post_collects` ADD `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_post_collects` ADD `id` BIGINT NOT NULL;
        ALTER TABLE `t_post_likes` ADD `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_post_likes` ADD `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_post_likes` ADD `id` BIGINT NOT NULL;
        ALTER TABLE `t_post_pictures` ADD `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_post_pictures` ADD `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_post_pictures` ADD `id` BIGINT NOT NULL;
        ALTER TABLE `t_user` ADD `created_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_user` ADD `updated_at` DATETIME(6) NOT NULL  DEFAULT CURRENT_TIMESTAMP(6) ON UPDATE CURRENT_TIMESTAMP(6);
        ALTER TABLE `t_user` ADD `id` BIGINT NOT NULL;
        ALTER TABLE `t_user_preference` ADD `id` BIGINT NOT NULL;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `t_post` DROP COLUMN `created_at`;
        ALTER TABLE `t_post` DROP COLUMN `updated_at`;
        ALTER TABLE `t_post` DROP COLUMN `id`;
        ALTER TABLE `t_user` DROP COLUMN `created_at`;
        ALTER TABLE `t_user` DROP COLUMN `updated_at`;
        ALTER TABLE `t_user` DROP COLUMN `id`;
        ALTER TABLE `t_muscle` DROP COLUMN `created_at`;
        ALTER TABLE `t_muscle` DROP COLUMN `updated_at`;
        ALTER TABLE `t_muscle` DROP COLUMN `id`;
        ALTER TABLE `t_comment` DROP COLUMN `created_at`;
        ALTER TABLE `t_comment` DROP COLUMN `updated_at`;
        ALTER TABLE `t_comment` DROP COLUMN `id`;
        ALTER TABLE `t_body_data` DROP COLUMN `created_at`;
        ALTER TABLE `t_body_data` DROP COLUMN `updated_at`;
        ALTER TABLE `t_body_data` DROP COLUMN `id`;
        ALTER TABLE `t_followers` DROP COLUMN `created_at`;
        ALTER TABLE `t_followers` DROP COLUMN `updated_at`;
        ALTER TABLE `t_followers` DROP COLUMN `id`;
        ALTER TABLE `t_post_likes` DROP COLUMN `created_at`;
        ALTER TABLE `t_post_likes` DROP COLUMN `updated_at`;
        ALTER TABLE `t_post_likes` DROP COLUMN `id`;
        ALTER TABLE `t_comment_likes` DROP COLUMN `created_at`;
        ALTER TABLE `t_comment_likes` DROP COLUMN `updated_at`;
        ALTER TABLE `t_comment_likes` DROP COLUMN `id`;
        ALTER TABLE `t_post_collects` DROP COLUMN `created_at`;
        ALTER TABLE `t_post_collects` DROP COLUMN `updated_at`;
        ALTER TABLE `t_post_collects` DROP COLUMN `id`;
        ALTER TABLE `t_post_pictures` DROP COLUMN `created_at`;
        ALTER TABLE `t_post_pictures` DROP COLUMN `updated_at`;
        ALTER TABLE `t_post_pictures` DROP COLUMN `id`;
        ALTER TABLE `t_history_uploads` DROP COLUMN `id`;
        ALTER TABLE `t_user_preference` DROP COLUMN `id`;"""
