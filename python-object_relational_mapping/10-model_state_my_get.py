#!/usr/bin/python3
"""
Module that prints the State object with the name passed as argument
from the database hbtn_0e_6_usa using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def get_state_by_name(username, password, db_name, state_name):
    """
    Connects to MySQL database and prints the id of the State
    matching the given name, or 'Not found' if it doesn't exist.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    state = session.query(State).filter(State.name == state_name).first()
    
    if state:
        print("{}".format(state.id))
    else:
        print("Not found")
        
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        get_state_by_name(
            sys.argv[1],
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
        )