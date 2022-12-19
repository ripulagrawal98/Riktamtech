from jproperties import Properties
configs = Properties()

with open('sqlqueries.properties','rb') as read_prop:
    configs.load(read_prop)

USER_CHECK=configs.get("user_check").data
USER_ROLE=configs.get("user_role").data
GROUP_NAME=configs.get("group_name").data
USER_NAME_ROLE=configs.get("user_name_role").data
GP_NAME_DIST=configs.get("gp_name_unique").data
USER_GROUP=configs.get("usr_group").data
USER_ID=configs.get("userid").data
GROUP_ID=configs.get("groupid").data
MESSAGE_USER=configs.get("message_user").data
USER_ALL=configs.get("all_users").data
USER_CHECK_INGRP=configs.get("usr_check_ingroup").data

##Insertion
INSERT_USER = configs.get("insert_user").data
INSERT_GROUP = configs.get("insert_group").data
INSERT_MESSAGE = configs.get("insert_message").data


## Deletion
DELETE_USER = configs.get("delete_user").data
DELETE_USER_GROUP=configs.get("delete_user_group").data