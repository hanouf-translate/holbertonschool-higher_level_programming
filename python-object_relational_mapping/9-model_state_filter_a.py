#!/usr/bin/python3
"""
Module that lists all State objects that contain the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def filter_states_with_a(username, password, db_name):
    """
    Connects to MySQL database and prints all State objects
    containing the letter 'a', ordered by id in ascending order.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    states = session.query(State).filter(
        State.name.like('%a%')
    ).order_by(State.id.asc()).all()
    
    for state in states:
        print("{}: {}".format(state.id, state.name))
        
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        filter_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])