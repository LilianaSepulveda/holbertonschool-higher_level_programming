#!/usr/bin/python3
"""
Module doc


"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """it file dont permite to be executed whe import
    """
    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=argv[1],
                           passwd=argv[2],
                           db=argv[3],
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT cities.name \
                 FROM cities \
                 INNER JOIN states \
                 ON cities.state_id=states.id \
                 WHERE states.name = %s \
                 ORDER BY cities.id ASC", (argv[4],))
    query_rows = cur.fetchall()
    for row in range(len(query_rows)):
        print(''.join(query_rows[row]), end="")
        if row < len(query_rows) - 1:
            print(", ", end="")
    print()

    cur.close()
    conn.close()
