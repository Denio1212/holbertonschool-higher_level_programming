#!/usr/bin/python3
"""
The model of a state
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class State(Base):
    """
    Inherits from the dec base
    """
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
