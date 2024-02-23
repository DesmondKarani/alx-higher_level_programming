#!/usr/bin/python3
"""
A script that lists all states from the database hbtn_0e_0_usa.
Usage: ./0-select_states.py <mysql username> <mysql password> <database name>
"""

import MySQLdb
import sys


def list_states(username, password, dbname):
    """
    Connects to a MySQL database and lists all states
    sorted in ascending order by id.
    """
    db = MySQLdb.connect(host="localhost",
                         port=3306, user=username, passwd=password, db=dbname)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])
