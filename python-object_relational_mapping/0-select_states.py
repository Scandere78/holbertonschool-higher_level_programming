#!/usr/bin/python3

import MySQLdb
import sys

def connectDb(user, password,db):
    """
        script that lists all states from the database hbtn_0e_0_usa
    """

    conn = MySQLdb.connect(                                                                                                 host="localhost",                                                                                               port=3306,
            user=user,                                                                            
            passwd=password,                                                                                                db=db,
            charset="utf8")
    
    return conn 


if __name__ == "__main__":

    user = sys.argv[1]
    password = sys.argv[2]
    db = sys.argv[3]

    conn = connectDb(user, password, db)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cursor.fetchall()
    for row in query_rows:
        print(row)

    cursor.close()
    conn.close()
