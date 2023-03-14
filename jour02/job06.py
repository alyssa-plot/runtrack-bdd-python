import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "azerty",
    database = "laplateforme"
)

cursor = db.cursor()
cursor.execute("SELECT sum(capacite) FROM salles")

aff = cursor.fetchone()
print("La capacité de toutes les salles est de:", aff[0])