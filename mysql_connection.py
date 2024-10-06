import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="root", password="Mysql@01", database="sakila")

mycursor = mydb.cursor()
mycursor.execute("select * from language")
result = mycursor.fetchall()
for i in result:
    print(i)