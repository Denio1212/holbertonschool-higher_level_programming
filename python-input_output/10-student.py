#!/usr/bin/python3
"""
Added function to retrieve attributes
"""


class Student:
    """
    class time
    """
    def __init__(self, first_name, last_name, age):
        """
        initer time
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves attributes too
        """
        if attrs is not None:
            new_dict = {}
            for i in attrs:
                for i in self.__dict__:
                    new_dict[i] = self.__dict__[i]
            return new_dict
        return self.__dict__
