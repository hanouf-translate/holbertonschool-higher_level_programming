#!/usr/bin/python3
"""
Module that takes in an argument and displays all values in the states
table of hbtn_0e_0_usa where name matches the argument.
"""

import sys
import MySQLdb


def filter_state_by_name(username, password, db_name, state_name):
    """
    Connects to MySQL and prints states where the name matches
    the provided argument, ordered by id in ascending order.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    
    cursor = db.cursor()
    query = (
        "SELECT * FROM states WHERE name LIKE BINARY '{}' "
        "ORDER BY id ASC;".format(state_name)
    )
    cursor.execute(query)
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_state_by_name(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
        )