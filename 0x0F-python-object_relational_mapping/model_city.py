#!/usr/bin/python3
# Inherits from SQLAlchemy Base and links to the MySQL table cities
"""
Module doc


"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """City for MySQL database
    __tablename__: MySQL table to store cities
        """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
