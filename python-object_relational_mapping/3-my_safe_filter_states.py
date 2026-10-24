#!/usr/bin/python3
"""
Module that safely filters states by user input,
protecting against SQL injection vulnerabilities.
"""

import sys
import MySQLdb


def safe_filter_states(username, password, db_name, state_name):
    """
    Connects to MySQL and safely prints states where the name matches
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
    # Using parameterized query (%s) to safely pass user input and prevent SQL injection
    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC;"
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        safe_filter_states(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
        )