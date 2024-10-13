from tortoise import BaseDBAsyncClient


async def upgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `t_user_preference` DROP INDEX `idx_t_user_pref_id_ec44c1`;
        ALTER TABLE `t_user` DROP INDEX `idx_t_user_id_49a745`;
        ALTER TABLE `t_user` DROP INDEX `idx_t_user_user_na_33a344`;
        ALTER TABLE `t_user` DROP INDEX `idx_t_user_be_foll_5c25fd`;
        ALTER TABLE `t_user` DROP INDEX `idx_t_user_created_9700b0`;
        ALTER TABLE `t_user` DROP INDEX `idx_t_user_likes_n_2429fe`;
        ALTER TABLE `t_user` DROP INDEX `idx_t_user_collect_9bbcd8`;
        ALTER TABLE `t_user` DROP INDEX `idx_t_user_be_coll_397277`;
        ALTER TABLE `t_user` DROP INDEX `idx_t_user_updated_ade55c`;
        ALTER TABLE `t_user` DROP INDEX `idx_t_user_be_like_b0be03`;
        ALTER TABLE `t_user` DROP INDEX `idx_t_user_followe_2bf6fe`;
        ALTER TABLE `t_user` DROP INDEX `idx_t_user_gender_778006`;
        ALTER TABLE `t_post_pictures` DROP INDEX `idx_t_post_pict_id_5b6fd1`;
        ALTER TABLE `t_post_pictures` DROP INDEX `idx_t_post_pict_created_c00986`;
        ALTER TABLE `t_post_pictures` DROP INDEX `idx_t_post_pict_updated_cb0718`;
        ALTER TABLE `t_post_likes` DROP INDEX `idx_t_post_like_id_594f11`;
        ALTER TABLE `t_post_likes` DROP INDEX `idx_t_post_like_created_2785fe`;
        ALTER TABLE `t_post_likes` DROP INDEX `idx_t_post_like_updated_3785f1`;
        ALTER TABLE `t_post_collects` DROP INDEX `idx_t_post_coll_id_1ad532`;
        ALTER TABLE `t_post_collects` DROP INDEX `idx_t_post_coll_created_3c5621`;
        ALTER TABLE `t_post_collects` DROP INDEX `idx_t_post_coll_updated_d6b869`;
        ALTER TABLE `t_post` DROP INDEX `idx_t_post_id_90e64a`;
        ALTER TABLE `t_post` DROP INDEX `idx_t_post_likes_n_d79510`;
        ALTER TABLE `t_post` DROP INDEX `idx_t_post_created_19a018`;
        ALTER TABLE `t_post` DROP INDEX `idx_t_post_title_3c14af`;
        ALTER TABLE `t_post` DROP INDEX `idx_t_post_collect_51e9d7`;
        ALTER TABLE `t_post` DROP INDEX `idx_t_post_updated_ff8418`;
        ALTER TABLE `t_post` DROP INDEX `idx_t_post_comment_4e0475`;
        ALTER TABLE `t_muscle` DROP INDEX `idx_t_muscle_id_0de3fd`;
        ALTER TABLE `t_muscle` DROP INDEX `idx_t_muscle_created_5fa821`;
        ALTER TABLE `t_muscle` DROP INDEX `idx_t_muscle_updated_de3195`;
        ALTER TABLE `t_history_uploads` DROP INDEX `idx_t_history_u_id_ae52ed`;
        ALTER TABLE `t_followers` DROP INDEX `idx_t_followers_id_77d93d`;
        ALTER TABLE `t_followers` DROP INDEX `idx_t_followers_created_952c96`;
        ALTER TABLE `t_followers` DROP INDEX `idx_t_followers_updated_9f9a65`;
        ALTER TABLE `t_comment_likes` DROP INDEX `idx_t_comment_l_id_753432`;
        ALTER TABLE `t_comment_likes` DROP INDEX `idx_t_comment_l_user_id_be50a5`;
        ALTER TABLE `t_comment_likes` DROP INDEX `idx_t_comment_l_to_comm_1b0eb8`;
        ALTER TABLE `t_comment_likes` DROP INDEX `idx_t_comment_l_created_642fc3`;
        ALTER TABLE `t_comment_likes` DROP INDEX `idx_t_comment_l_updated_a339e7`;
        ALTER TABLE `t_comment` DROP INDEX `idx_t_comment_id_1e66f9`;
        ALTER TABLE `t_comment` DROP INDEX `idx_t_comment_created_7ab37f`;
        ALTER TABLE `t_comment` DROP INDEX `idx_t_comment_level_878f0c`;
        ALTER TABLE `t_comment` DROP INDEX `idx_t_comment_father__28475f`;
        ALTER TABLE `t_comment` DROP INDEX `idx_t_comment_updated_e71593`;
        ALTER TABLE `t_body_data` DROP INDEX `idx_t_body_data_id_ebd3f5`;
        ALTER TABLE `t_body_data` DROP INDEX `idx_t_body_data_created_a51412`;
        ALTER TABLE `t_body_data` DROP INDEX `idx_t_body_data_updated_9af245`;"""


async def downgrade(db: BaseDBAsyncClient) -> str:
    return """
        ALTER TABLE `t_post` ADD INDEX `idx_t_post_comment_4e0475` (`comments_num`);
        ALTER TABLE `t_post` ADD INDEX `idx_t_post_updated_ff8418` (`updated_at`);
        ALTER TABLE `t_post` ADD INDEX `idx_t_post_collect_51e9d7` (`collects_num`);
        ALTER TABLE `t_post` ADD INDEX `idx_t_post_title_3c14af` (`title`);
        ALTER TABLE `t_post` ADD INDEX `idx_t_post_created_19a018` (`created_at`);
        ALTER TABLE `t_post` ADD INDEX `idx_t_post_likes_n_d79510` (`likes_num`);
        ALTER TABLE `t_post` ADD INDEX `idx_t_post_id_90e64a` (`id`);
        ALTER TABLE `t_user` ADD INDEX `idx_t_user_gender_778006` (`gender`);
        ALTER TABLE `t_user` ADD INDEX `idx_t_user_followe_2bf6fe` (`followers_num`);
        ALTER TABLE `t_user` ADD INDEX `idx_t_user_be_like_b0be03` (`be_liked_num`);
        ALTER TABLE `t_user` ADD INDEX `idx_t_user_updated_ade55c` (`updated_at`);
        ALTER TABLE `t_user` ADD INDEX `idx_t_user_be_coll_397277` (`be_collected_num`);
        ALTER TABLE `t_user` ADD INDEX `idx_t_user_collect_9bbcd8` (`collects_num`);
        ALTER TABLE `t_user` ADD INDEX `idx_t_user_likes_n_2429fe` (`likes_num`);
        ALTER TABLE `t_user` ADD INDEX `idx_t_user_created_9700b0` (`created_at`);
        ALTER TABLE `t_user` ADD INDEX `idx_t_user_be_foll_5c25fd` (`be_followed_num`);
        ALTER TABLE `t_user` ADD INDEX `idx_t_user_user_na_33a344` (`user_name`);
        ALTER TABLE `t_user` ADD INDEX `idx_t_user_id_49a745` (`id`);
        ALTER TABLE `t_muscle` ADD INDEX `idx_t_muscle_updated_de3195` (`updated_at`);
        ALTER TABLE `t_muscle` ADD INDEX `idx_t_muscle_created_5fa821` (`created_at`);
        ALTER TABLE `t_muscle` ADD INDEX `idx_t_muscle_id_0de3fd` (`id`);
        ALTER TABLE `t_comment` ADD INDEX `idx_t_comment_updated_e71593` (`updated_at`);
        ALTER TABLE `t_comment` ADD INDEX `idx_t_comment_father__28475f` (`father_comment_id`);
        ALTER TABLE `t_comment` ADD INDEX `idx_t_comment_level_878f0c` (`level`);
        ALTER TABLE `t_comment` ADD INDEX `idx_t_comment_created_7ab37f` (`created_at`);
        ALTER TABLE `t_comment` ADD INDEX `idx_t_comment_id_1e66f9` (`id`);
        ALTER TABLE `t_body_data` ADD INDEX `idx_t_body_data_updated_9af245` (`updated_at`);
        ALTER TABLE `t_body_data` ADD INDEX `idx_t_body_data_created_a51412` (`created_at`);
        ALTER TABLE `t_body_data` ADD INDEX `idx_t_body_data_id_ebd3f5` (`id`);
        ALTER TABLE `t_followers` ADD INDEX `idx_t_followers_updated_9f9a65` (`updated_at`);
        ALTER TABLE `t_followers` ADD INDEX `idx_t_followers_created_952c96` (`created_at`);
        ALTER TABLE `t_followers` ADD INDEX `idx_t_followers_id_77d93d` (`id`);
        ALTER TABLE `t_post_likes` ADD INDEX `idx_t_post_like_updated_3785f1` (`updated_at`);
        ALTER TABLE `t_post_likes` ADD INDEX `idx_t_post_like_created_2785fe` (`created_at`);
        ALTER TABLE `t_post_likes` ADD INDEX `idx_t_post_like_id_594f11` (`id`);
        ALTER TABLE `t_comment_likes` ADD INDEX `idx_t_comment_l_updated_a339e7` (`updated_at`);
        ALTER TABLE `t_comment_likes` ADD INDEX `idx_t_comment_l_created_642fc3` (`created_at`);
        ALTER TABLE `t_comment_likes` ADD INDEX `idx_t_comment_l_to_comm_1b0eb8` (`to_comment_id`);
        ALTER TABLE `t_comment_likes` ADD INDEX `idx_t_comment_l_user_id_be50a5` (`user_id`);
        ALTER TABLE `t_comment_likes` ADD INDEX `idx_t_comment_l_id_753432` (`id`);
        ALTER TABLE `t_post_collects` ADD INDEX `idx_t_post_coll_updated_d6b869` (`updated_at`);
        ALTER TABLE `t_post_collects` ADD INDEX `idx_t_post_coll_created_3c5621` (`created_at`);
        ALTER TABLE `t_post_collects` ADD INDEX `idx_t_post_coll_id_1ad532` (`id`);
        ALTER TABLE `t_post_pictures` ADD INDEX `idx_t_post_pict_updated_cb0718` (`updated_at`);
        ALTER TABLE `t_post_pictures` ADD INDEX `idx_t_post_pict_created_c00986` (`created_at`);
        ALTER TABLE `t_post_pictures` ADD INDEX `idx_t_post_pict_id_5b6fd1` (`id`);
        ALTER TABLE `t_history_uploads` ADD INDEX `idx_t_history_u_id_ae52ed` (`id`);
        ALTER TABLE `t_user_preference` ADD INDEX `idx_t_user_pref_id_ec44c1` (`id`);"""
