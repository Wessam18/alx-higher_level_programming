#!/usr/bin/python3
"""import modules"""

from sqlalchemy import INTEGER, String, Column
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """class State"""
    __tablename__ = "states"
    id = Column(INTEGER, primary_key=True, nullable=False,
                unique=True, autoincrement=True)
    name = Column(String(128), nullable=False)
