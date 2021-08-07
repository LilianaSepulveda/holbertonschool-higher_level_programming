#!/usr/bin/python3
# List all states from database hbtn_0e_0usa

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for states in query_rows:
        print(states)

cur.close()
db.close()
