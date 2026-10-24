#!/usr/bin/python3
"""
Module that lists all cities of a given state from the database hbtn_0e_4_usa.
SQL injection free.
"""

import sys
import MySQLdb


def filter_cities_by_state(username, password, db_name, state_name):
    """
    Connects to MySQL and prints all cities of a given state separated by commas,
    ordered by cities.id ASC, using a single parameterized query.
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
        "SELECT cities.name "
        "FROM cities "
        "JOIN states ON cities.state_id = states.id "
        "WHERE states.name = %s "
        "ORDER BY cities.id ASC;"
    )
    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    
    # Extract city names and join them with comma and space
    cities_list = [row[0] for row in rows]
    print(", ".join(cities_list))
        
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        filter_cities_by_state(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
        )