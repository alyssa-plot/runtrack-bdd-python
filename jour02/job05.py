import mysql.connector

db = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "azerty",
    database = "laplateforme"
)

cursor = db.cursor()
cursor.execute("SELECT sum(superficie) FROM etage")

aff = cursor.fetchone()
print("La superficie de La Plateforme est de", aff[0],"m²")