import dbconn
import SQL

mydb = dbconn.dbConn
mysql = dbconn.mySql

## method to fetch groupName on the basis of userName
def fetch_group_name(userName):

    group_sql = SQL.GROUP_NAME
    data = [userName]
    mysql.execute(group_sql,data)

    group_list = []
    groups = mysql.fetchall()
    if len(groups)>0 :
        for group in groups:
            group_list.append(group[0])
    
    return group_list


## Check if user already exist
def user_exist(userName):
    user_check = SQL.USER_CHECK
    val = [userName]
    
    mysql.execute(user_check,val)

    if len(mysql.fetchall())>0:
       
        return 1
    else:
        return 0

def user_exist_ingroup(userName,groupName):

    user_check = SQL.USER_CHECK_INGRP
    val=[userName,groupName]
    mysql.execute(user_check,val)
    if len(mysql.fetchall())>0:
        return 1
    else:
        return 0

def fetch_user_details(userName):
    user_search = SQL.USER_CHECK
    val = [userName]

    mysql.execute(user_search,val)
    result = mysql.fetchall()
    return result

def get_user_role(userName):
    userRole_sql = SQL.USER_ROLE
    user = [userName]
    mysql.execute(userRole_sql,user)

    # if userRole is 0 --> Normal User
    # userRole == 1 --> Admin User
    userRole = mysql.fetchall()[0][0]
    return userRole


def get_normalUsers():
    users_sql = SQL.USER_NAME_ROLE
    type=[0]
    mysql.execute(users_sql,type)
    users= mysql.fetchall()
    return users

def getallUsers():
    users_sql=SQL.USER_ALL
    mysql.execute(users_sql)
    users=mysql.fetchall()
    return users


def fetch_unique_groups():
    group_sql = SQL.GP_NAME_DIST
    
    mysql.execute(group_sql)

    groups= mysql.fetchall()
    return groups

def get_userby_group(group):
    user_sql = SQL.USER_GROUP

    gg = [group]
    mysql.execute(user_sql,gg)

    users= mysql.fetchall()
    return users

def get_groupID(groupName):
    gp_id_sql = SQL.GROUP_ID
    
    arg = [groupName]
    mysql.execute(gp_id_sql,arg)
    gp_id=mysql.fetchall()[0][0]
    return gp_id


def get_msg_user(groupName):
    msg_sql = SQL.MESSAGE_USER
    data = [groupName]
    mysql.execute(msg_sql,data)

    msgs = mysql.fetchall()
    return msgs

def get_userID(user):
    userID_sql  = SQL.USER_ID
    data = [user]
    mysql.execute(userID_sql,data)
    
    userID = mysql.fetchall()[0][0]
    return userID

## Insertion functions

def insert_user(userName,userRole,password):
    try:
        usr_ins_sql = SQL.INSERT_USER 
        val = (userName,userRole,password)
        mysql.execute(usr_ins_sql,val)
        mydb.commit();
        return 1
    except print(0):
        return 0
        pass

def insert_message(message,groupName,userName):
    try:
        insert_msg_sql = SQL.INSERT_MESSAGE
        data = [message,groupName,userName]

        mysql.execute(insert_msg_sql,data)

        mydb.commit()
        return 1
    except print(0):
        return 0
        pass

def insert_group(group,user,userID):
   
   try:
        group_sql = SQL.INSERT_GROUP
        data = [group,user,userID]

        mysql.execute(group_sql,data)
        mydb.commit()

        return 1
   except print(0):
        return 0
        pass

def delete_user(user_del):
    
    try:
        delete_sql = SQL.DELETE_USER
        user=(user_del,)

        mysql.execute(delete_sql,user)
        mydb.commit()
        return 1
    except print(0):
        return 0
        pass

def delete_user_ingrp(userName,groupName):
    
    try:
        delete_user=SQL.DELETE_USER_GROUP
        arg = [userName,groupName]
        mysql.execute(delete_user,arg)
        mydb.commit()
        return 1
    except print(0):
        return 0
        pass
    