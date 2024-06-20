#!/usr/bin/python3
import MySQLdb
import sys
if _name_ == "_main_":
    
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

db = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")

cursor = db.cursor()

cursor.execute("SELECT * FROM states ORDER BY id ASC")

rows = cursor.fetchall()

for row in rows:
    print(row)

cursor.close()
db.close()

