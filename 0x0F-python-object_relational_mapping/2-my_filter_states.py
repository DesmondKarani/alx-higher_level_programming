#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username>
<mysql password> <database name> <state name>
"""

import MySQLdb
import sys


def filter_states_by_user_input(username, password, dbname, state_name):
    """
    Connects to a MySQL database and lists all states where the name matches
    the user-provided state name, sorted in ascending order by id.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=dbname
    )
    cur = db.cursor()
    query = (
            "SELECT * FROM states"
            "WHERE name = '{}'"
            "ORDER BY id ASC"
            ).format(state_name)
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        if row[1] == state_name:
            print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_states_by_user_input(
                sys.argv[1],
                sys.argv[2],
                sys.argv[3],
                sys.argv[4]
                )
