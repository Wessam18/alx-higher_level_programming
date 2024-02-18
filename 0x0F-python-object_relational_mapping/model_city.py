#!/usr/bin/python3
"""
class definition of a State and an instance Base = declarative_base()
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
    A class representing the state table in the database.
    """
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
