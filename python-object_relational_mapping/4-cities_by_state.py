#!/usr/bin/python3
"""
Module that lists all cities from the database hbtn_0e_4_usa
joined with their respective states, ordered by cities.id.
"""

import sys
import MySQLdb


def list_cities_by_state(username, password, db_name):
    """
    Connects to MySQL and prints all cities with their state names
    using a single JOIN query, ordered by cities.id ASC.
    """
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=db_name
    )
    
    cursor = db.cursor()
    # Using a single JOIN query to fetch city id, city name, and state name
    query = (
        "SELECT cities.id, cities.name, states.name "
        "FROM cities JOIN states ON cities.state_id = states.id "
        "ORDER BY cities.id ASC;"
    )
    cursor.execute(query)
    rows = cursor.fetchall()
    
    for row in rows:
        print(row)
        
    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        list_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])