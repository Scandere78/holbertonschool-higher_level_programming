#!/usr/bin/python3
import mysql.connector
import sys

if __name__ == "__main__":
    # Récupérer les arguments de la ligne de commande
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    
    # Connexion à la base de données MySQL
    db = mysql.connector.connect(
        host="localhost",
        user=mysql_username,
        passwd=mysql_password,
        database=database_name
    )
    
    # Création d'un curseur pour exécuter les requêtes
    cursor = db.cursor()
    
    # Exécution de la requête pour récupérer les états dont le nom commence par 'N'
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    
    # Récupérer tous les résultats de la requête
    rows = cursor.fetchall()
    
    # Affichage des résultats
    for row in rows:
        print(row)
    
    # Fermeture du curseur et de la connexion à la base de données
    cursor.close()
    db.close()

