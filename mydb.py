import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'M1d1t3c4'

)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE elderco")

print("All Done!")