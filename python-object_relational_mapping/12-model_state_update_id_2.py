#!/usr/bin/python3
"""
Module that changes the name of a State object from the database hbtn_0e_6_usa
where id = 2 to "New Mexico" using SQLAlchemy.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def update_state(username, password, db_name):
    """
    Connects to MySQL database, queries the State object with id = 2,
    updates its name to "New Mexico", and commits the changes.
    """
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            username, password, db_name
        ),
        pool_pre_ping=True
    )
    
    Session = sessionmaker(bind=engine)
    session = Session()
    
    state = session.query(State).filter(State.id == 2).first()
    if state:
        state.name = "New Mexico"
        session.commit()
        
    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        update_state(sys.argv[1], sys.argv[2], sys.argv[3])