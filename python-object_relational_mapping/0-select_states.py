#!/usr/bin/python3
"""
Module that lists all states from the database hbtn_0e_0_usa.
Connects to a MySQL server running on localhost at port 3306.
"""

import sys
import MySQLdb


def list_states(username, password, db_name):
    """
    Connects to MySQL and prints all states from the states table
    ordered by id in ascending order.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    
    cursor = db.cursor()
    cursor.execute("SELECT id, name FROM states ORDER BY id ASC;")
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_states(sys.argv[1], sys.argv[2], sys.argv[3])