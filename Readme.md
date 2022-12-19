# Pre-requisite
* Python 3 must be installed
* MySQL client must be installed to check DB (no need to create DB and tables as already running on cloud)

# Project Details
* app.py --> Main Program 
* dbconn.py --> Handles DB connection
* sqlqueries.properties --> DB queries related to application
* SQL.py    --> Program to load all the db queries at runtime from properties
* db_functions.py --> Takes care of DB query execution basically DAO layer for this application
* testcases/
  * group_message_app_testcases.xlsx --> Testcases to run on application

* templates/
  * signUp.html --> SignUp Page */Welcome* endpoint
  * login.html --> Login Page */loginUser* endpoint
  * adminUserMgmt.html --> Manage UserPage for admin users only */usermgmt* endpoint
  * userMgmt.html  --> Manage UserPage for Normal Users */usermgmt* endpoint
  * manageGroup.html --> Manage Group Page for all users */manageGroup* & */creatGroup* endpoint 
  * messaging.html --> Messaging Page for users to chat */groupMsg* & */sendMessage* endpoint
  
# Important Points
* During User Creation please use **admin** as user Type to create admin user & **normal** for normal user

# DB Details
* Host: mysql-101015-0.cloudclusters.net
* Port: 10132
* IP Address: 68.64.164.113
* Super User: admin
* Password: CtA4GXZY

# Steps to Run the application
* Clone the repository in local machine
* Navigate to directory where cloned the project
* Install the required packages ` pip install -r requirements. txt `
* open command prompt and run `python app.py`
* open browser and hit *http://127.0.0.1:8080/Welcome*

