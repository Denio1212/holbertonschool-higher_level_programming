#!/usr/bin/python3
""" Creating the state class"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    ''' Inheriting from Base class'''
    id = Column(Integer, nullable=False, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)
