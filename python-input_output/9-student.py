#!/usr/bin/python3
"""
A student class that is defined by name and age
"""


class Student:
    """
    Our students
    """
    def __init__(self, first_name, last_name, age):
        """
        Initializer
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        retrieves dict representation
        """
        return self.__dict__
