#!/usr/bin/python3
# Inherits from SQLAlchemy Base and links to the MySQL table states
"""
Module doc


"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """State for a MySQL database
    __tablename__: MySQL table to store States
        """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
