# https://nordicapis.com/how-to-create-an-api-using-the-flask-framework/
# https://codeburst.io/jinja-2-explained-in-5-minutes-88548486834e
# https://www.w3schools.com/howto/howto_js_popup_chat.asp

import dbconn,SQL,db_functions

from flask import Flask,render_template,request,jsonify,redirect,session
from flask import json

from flask_session import Session


app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

mydb = dbconn.dbConn
mysql = dbconn.mySql

### Welcome Page EndPoint
@app.route('/Welcome',methods=['GET'])
def Welcome():
    return render_template('signUp.html')

### Signup Page endpoint
@app.route('/createUser',methods=['POST'])
def addUser():
    userName = request.form['UserName']
    password = request.form['password']
    userType = request.form['userType']

    if userType == "admin":
        userRole = 1
    else:
        userRole = 0
 
    user_check = db_functions.user_exist(userName)
    if user_check=="SUCCESS":
        print("User exist")
        results = {
            "Error" : "User Already Exists"
        }
        return render_template('signUp.html',results=results)


    user_insert = db_functions.insert_user(userName,userRole,password)
    if user_insert==1:
        print("User Creation success")
    else:
        print("User Creation Failed due to DB error")

    return redirect('/loginUser')
    

# Login page end point
@app.route('/loginUser')
def loginpage():
    return render_template('login.html')

##login page end point
@app.route('/login',methods=['POST'])
def authenticate():

    userName = request.form['userName']
    password = request.form['password']  

    user_search = db_functions.user_exist
    
    if user_search == 0:
       results = {
        "Error" : "User Not Found"
       }
       return render_template('login.html',results)
    else :
        user_details = db_functions.fetch_user_details(userName)
        for res in user_details :
            username=res[1]
            userPass=res[3]
            userRole=res[2]
    
    if userPass!=password :
        results = {
        "Error" : "Wrong Password"
       }
        return render_template('login.html',results)
    else:
        session['userName']=userName
        

    return redirect('/usermgmt')
    
### EndPoint gets call when login Success
@app.route('/usermgmt')
def userManage():

    if not session.get("userName"):
        return redirect("/loginUser")

    userName = session.get("userName")

    userRole = db_functions.get_user_role(userName)

    group_list = db_functions.fetch_group_name(userName)
    
    if userRole==1:
       
        users = db_functions.get_normalUsers()
        user_list = []
        i = 0
        for user in users:
            user_list.append(user[0])
            
        userdetails = {
            "admin" : userName,
            "Users" : user_list,
            "Groups" : group_list
        }
        return render_template('adminUserMgmt.html',results=userdetails)
    
    else :
        userdetails = {
            "user" : userName,
            "Groups" : group_list
        }
        
    
    return render_template('userMgmt.html',results=userdetails)
    
### End Point to delete user by AdminUser
@app.route('/delete',methods=['POST'])
def deleteUser():
   
    user_del = request.form['userName']

    delete_res = db_functions.delete_user(user_del)

    if delete_res==1:
        print("User Deletion Success")
    else:
        print("User deletion Failed")

    return redirect('/usermgmt')


## End point to Manage Group
@app.route('/manageGroup')
def ManageGroup():
    
    if not session.get("userName"):
        return redirect("/loginUser")
    userName = session.get("userName")

    
    groups = db_functions.fetch_unique_groups()
    users = db_functions.getallUsers()
    group_current_user = db_functions.fetch_group_name(userName)

    alluser_list = []
    if len(users)>0:
        for user in users:
            alluser_list.append(user[0])
    
    if len(groups)>0:
        group_list = []
        i = 0
        for group in groups:
            group_list.append(group[0])
           
    
        Group_list = []
        for group in group_list:
          
            users = db_functions.get_userby_group(group)
            user_list = []
            i = 0
            for user in users:
                user_list.append(user[0])
                
    
            groupDetails = {
                "Group" : group,
                "Users" : user_list
            } 
            Group_list.append(groupDetails)
        
        results = {
        "Groups" : Group_list,
        "Users" : alluser_list,
        "GRP_USR" : group_current_user,
        "CurrentUser" : userName
        }

        return render_template('manageGroup.html',results = results)    
    else :
        Group_list = []

    results = {
        "Groups" : Group_list,
        "Users" : alluser_list,
        "GRP_USR" : group_current_user,
        "CurrentUser" : userName
    }
   
    return render_template('manageGroup.html',results=results)


## End Point to create New Group
@app.route('/createGroup',methods=["POST"])
def CreateGroup():
    if not session.get("userName"):
        return redirect("/loginUser")
    
    userName = session.get("userName")
    group = request.form['group']
    user = request.form['user']
    group_current_user = db_functions.fetch_group_name(userName)
    
    userID = db_functions.get_userID(user)

    user_exist=db_functions.user_exist_ingroup(user,group)

    if user_exist==1:
        error_list=["User Already Present in group"]
    else:
        error_list = []
        group_ins = db_functions.insert_group(group,user,userID)
        if group_ins==1:
            print("Group Created")

        else:
            print("Group Failed")

    users = db_functions.getallUsers()
    alluser_list = []
    if len(users)>0:
        for user in users:
            alluser_list.append(user[0])

    ## Fetch all the groups Present in DB
    
    groups = db_functions.fetch_unique_groups()
    
    
    if len(groups)>0:
        group_list = []
        i = 0
        for group in groups:
            group_list.append(group[0])
            
    
        Group_list = []
        for group in group_list:
           
            users = db_functions.get_userby_group(group)
            user_list = []
            i = 0
            for user in users:
                user_list.append(user[0])
    
            groupDetails = {
                "Group" : group,
                "Users" : user_list
            } 
            Group_list.append(groupDetails)
        results = {
        "Groups" : Group_list,
        "Users" : alluser_list,
         "GRP_USR" : group_current_user,
         "Errors" : error_list,
         "CurrentUser" : userName
        }
        return render_template('manageGroup.html',results = results)    
    else :
        Group_list = []

    results = {
        "Groups" : Group_list,
        "Users" : alluser_list,
         "GRP_USR" : group_current_user,
         "Errors" : error_list,
         "CurrentUser" : userName
        }
   
    return render_template('manageGroup.html',results=results)


@app.route('/deleteUsrGroup',methods=["POST"])
def deleteUsrGroup():
    userName = request.form['userName']
    groupName = request.form['groupName']

    del_usr = db_functions.delete_user_ingrp(userName,groupName)

    if del_usr==1:
        print("User "+userName+" Deleted from group "+groupName)
    else :
        print("User "+userName+" Deletion from group "+groupName+" failed")

    
    return redirect('/manageGroup')

@app.route('/groupMsg',methods=["POST"])
def messaging():
    if not session.get("userName"):
        return redirect("/loginUser")

    userName = session.get("userName")
    groupName = request.form['group']

    if not session.get("groupName"):
        session['groupName']=groupName
    elif session.get('groupName') != groupName:
        session['groupName']=groupName
    
    gp_id_sql = SQL.GROUP_ID
    arg = [groupName]
    mysql.execute(gp_id_sql,arg)
    gp_id=mysql.fetchall()[0][0]

    msgs = db_functions.get_msg_user(groupName)

    msg_list = []

    if len(msgs)>0:
        for msg in msgs:
            msg_detail = {
                "msg" : msg[0],
                "user" : msg[1]
            }
            msg_list.append(msg_detail)
            print("Message is ")
            print(msg[0])
    
    data = {
        "Group" : groupName,
        "User" : userName,
        "Msg" : msg_list
    }

    return render_template('/messaging.html',results = data)

@app.route('/sendMessage',methods=["POST"])
def sendMessage():

    if not session.get("userName"):
        return redirect("/loginUser")
    
    userName = session.get("userName")
    groupName = session.get("groupName")
    
    message = request.form['msg']
   
    gp_id = db_functions.get_groupID(groupName)

   
    msg_ins = db_functions.insert_message(message,groupName,userName)
    if msg_ins==1:
        print("Message Inserted")
    else:
        print("message insertion failed")

    msgs = db_functions.get_msg_user(groupName)

    msg_list = []

    if len(msgs)>0:
        for msg in msgs:
            msg_detail = {
                "msg" : msg[0],
                "user" : msg[1]
            }
            msg_list.append(msg_detail)
            
    data = {
        "Group" : groupName,
        "User" : userName,
        "Msg" : msg_list
    }

    return render_template('/messaging.html',results = data)
    
    
##logout endpoint
@app.route("/logout")
def logout():
    session["userName"] = None
    return redirect("/loginUser")




if __name__ == "__main__":
    app.run(port=8080)


