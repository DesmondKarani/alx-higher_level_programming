#!/usr/bin/python3
"""
A script that takes in an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument.
Usage: ./2-my_filter_states.py <mysql username>
<mysql password> <database name> <state name>
"""

import MySQLdb
import sys


def main():
    """Main function to list states from the database."""
    # Establish database connection
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1],
                                 passwd=sys.argv[2], db=sys.argv[3], port=3306)
    # Create cursor
    cursor = connection.cursor()
    # Execute query
    state_name = sys.argv[4]
    query = "SELECT * FROM states WHERE name LIKE BINARY %s"
    cursor.execute(query, (state_name,))
    # Fetch and print all rows
    for row in cursor.fetchall():
        print(row)
    # Close cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    main()
