#!/usr/bin/python3
"""
Module that adds the State object "Louisiana" to the database hbtn_0e_6_usa
using SQLAlchemy and prints the new state's id.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def insert_louisiana(username, password, db_name):
    """
    Connects to MySQL database, creates and adds a new State object for Louisiana,
    commits the session, and prints the newly generated id.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    
    print("{}".format(new_state.id))
        
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        insert_louisiana(sys.argv[1], sys.argv[2], sys.argv[3])