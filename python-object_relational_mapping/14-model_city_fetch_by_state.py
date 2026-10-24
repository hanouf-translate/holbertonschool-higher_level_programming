#!/usr/bin/python3
"""
Module that prints all City objects from the database hbtn_0e_14_usa
ordered by cities.id using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


def fetch_cities_by_state(username, password, db_name):
    """
    Connects to MySQL database and prints all City objects
    along with their corresponding State names.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    # Query cities joined with states, ordered by cities.id ascending
    results = session.query(City, State).join(
        State, City.state_id == State.id
    ).order_by(City.id.asc()).all()
    
    for city, state in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))
        
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        fetch_cities_by_state(sys.argv[1], sys.argv[2], sys.argv[3])