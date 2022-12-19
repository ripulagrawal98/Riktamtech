import mysql.connector

# dbConn = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="root@123",
#     database="Riktamtech"
# )

dbConn = mysql.connector.connect(
    host="mysql-101015-0.cloudclusters.net",
    port="10132",
    user="admin",
    password="CtA4GXZY",
    database="riktamtech"
)

mySql = dbConn.cursor()


