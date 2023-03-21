import mysql.connector
import csv
db = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "",
  database = "user"
)

# Ouvrir le fichier csv
with open('count.csv', 'r') as f:
    # Créer un objet csv à partir du fichier
    obj = csv.reader(f,delimiter=';')

    for ligne in obj:
        cur = db.cursor()
        #requéte SQL
        sql = "INSERT INTO user (username, fullname,email,contact) VALUES (%s, %s,%s,%s)"
        #exécuter le curseur avec la méthode execute() et transmis la requéte SQL
        print(ligne)
        cur.execute(sql, tuple(ligne))
        #valider la transaction
        db.commit()
        #afficher le nombre de lignes insérées
        print(cur.rowcount, "ligne insérée.")
