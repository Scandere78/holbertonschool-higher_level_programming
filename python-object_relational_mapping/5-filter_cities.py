#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host='localhost',
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3]
    )
    cur = db.cursor()
    query = """
    SELECT cities.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    WHERE states.name = %s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (sys.argv[4],))
    query_rows = cur.fetchall()

    if query_rows:
        print(", ".join(row[0] for row in query_rows))
    else:
        print("")

    cur.close()
    db.close()
