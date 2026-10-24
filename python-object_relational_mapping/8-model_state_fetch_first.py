#!/usr/bin/python3
"""
Module that prints the first State object from the database hbtn_0e_6_usa
using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def fetch_first_state(username, password, db_name):
    """
    Connects to MySQL database and prints the first State object
    ordered by id. Prints 'Nothing' if the table is empty.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    state = session.query(State).order_by(State.id.asc()).first()
    
    if state:
        print("{}: {}".format(state.id, state.name))
    else:
        print("Nothing")
        
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        fetch_first_state(sys.argv[1], sys.argv[2], sys.argv[3])