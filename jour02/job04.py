import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "azerty",
    database = "laplateforme"
)

cursor = db.cursor()
cursor.execute("SELECT * FROM salles")

aff = cursor.fetchall()
print(aff)