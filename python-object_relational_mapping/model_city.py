#!/usr/bin/python3
"""
Module that contains the class definition of a City
and links it to the MySQL table cities using SQLAlchemy.
"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """
    Represents a city for a MySQL database.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store cities.
        id (Column): The city's id, primary key, auto-generated integer,
                     not null.
        name (Column): The city's name, string of maximum 128 characters,
                       not null.
        state_id (Column): The foreign key referencing states.id, integer,
                           not null.
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)