#!/usr/bin/python3
"""
Module that contains the class definition of a State
and an instance Base = declarative_base().
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
    Represents a state for a MySQL database.
    
    Attributes:
        __tablename__ (str): The name of the MySQL table to store states.
        id (Column): The state's id, primary key, auto-generated integer,
                     not null.
        name (Column): The state's name, string of maximum 128 characters,
                       not null.
    """
    __tablename__ = 'states'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)