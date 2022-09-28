import mysql.connector

mydb = mysql.connector.connect(
    host="localhost"
    user="yourusername"
    password="yourpassword"
    database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM tablename")

myresult = mycursor.fetchall()

for x in myresult:
    print(x)
