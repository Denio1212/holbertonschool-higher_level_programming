#!/usr/bin/python3
"""model_city module
Contains the definition of a city
Foreign key that connects to the states.id and everything
else is similar to the state class
"""
from sqlalchemy.orm import relationship
from model_state import Base
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class
    The base class for any city
    """
    state = relationship("State")
    __tablename__ = "cities"
    id = Column(Integer, unique=True, nullable=False,
                primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, nullable=False, ForeignKey="states.id")

