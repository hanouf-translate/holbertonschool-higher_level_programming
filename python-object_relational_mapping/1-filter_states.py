#!/usr/bin/python3
"""
Module that lists all states with a name starting with 'N'
from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb


def filter_states(username, password, db_name):
    """
    Connects to MySQL and prints all states with a name starting
    with 'N' from the states table ordered by id in ascending order.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    
    cursor = db.cursor()
    # Using BINARY to ensure case-sensitive comparison for 'N'
    cursor.execute(
        "SELECT id, name FROM states WHERE name LIKE BINARY 'N%' "
        "ORDER BY id ASC;"
    )
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states(sys.argv[1], sys.argv[2], sys.argv[3])