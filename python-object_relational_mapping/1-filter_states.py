import MySQLdb
import sys
"""
script to connect DB
"""

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    
    conn = MySQLdb.connect(host="localhost", port=3306, user="root", passwd="root", db="my_db", charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states WHERE NAME LIKE 'N%' ORDER BY id ASC") 
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
    