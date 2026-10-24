#!/usr/bin/python3
"""
Module that deletes all State objects with a name containing the letter 'a'
from the database hbtn_0e_6_usa using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def delete_states_with_a(username, password, db_name):
    """
    Connects to MySQL database, queries all State objects containing 'a',
    deletes them, and commits the session changes.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    states = session.query(State).filter(State.name.like('%a%')).all()
    for state in states:
        session.delete(state)
        
    session.commit()
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        delete_states_with_a(sys.argv[1], sys.argv[2], sys.argv[3])