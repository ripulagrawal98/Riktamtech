import mysql.connector

dbConn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root@123",
    database="Riktamtech"
)

mySql = dbConn.cursor()


