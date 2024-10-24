from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `t_user_vital_capacity` DROP INDEX `uid_t_user_vita_user_id_91f44a`;
        ALTER TABLE `t_user_body_fat_rate` DROP INDEX `uid_t_user_body_user_id_f6d940`;
        ALTER TABLE `t_user_body_fat_rate` RENAME COLUMN `user_id` TO `record_id`;
        ALTER TABLE `t_user_body_fat_rate` ADD `user_id` VARCHAR(36) NOT NULL  COMMENT '用户ID';
        ALTER TABLE `t_user_vital_capacity` RENAME COLUMN `user_id` TO `record_id`;
        ALTER TABLE `t_user_vital_capacity` ADD `user_id` VARCHAR(36) NOT NULL  COMMENT '用户ID';"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `t_user_body_fat_rate` RENAME COLUMN `record_id` TO `user_id`;
        ALTER TABLE `t_user_body_fat_rate` DROP COLUMN `user_id`;
        ALTER TABLE `t_user_vital_capacity` RENAME COLUMN `record_id` TO `user_id`;
        ALTER TABLE `t_user_vital_capacity` DROP COLUMN `user_id`;
        ALTER TABLE `t_user_body_fat_rate` ADD UNIQUE INDEX `uid_t_user_body_user_id_f6d940` (`user_id`, `record_date`);
        ALTER TABLE `t_user_vital_capacity` ADD UNIQUE INDEX `uid_t_user_vita_user_id_91f44a` (`user_id`, `record_date`);"""
