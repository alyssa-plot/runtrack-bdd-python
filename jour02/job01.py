import mysql.connector

mydb = mysql.connector.connect(
    user='root',
    password='azerty',
    database='laplateforme'
)
cursor = mydb.cursor()
cursor.execute("SELECT * FROM `laplateforme`.`etudiants`")

resultats = cursor.fetchall()

for resultat in resultats:
    print(resultat)