#!/usr/bin/python3
"""
Added a se/deserializer
"""


class Student:
    """
    Good old class m8
    """

    def __init__(self, first_name, last_name, age):
        """
        initser
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        retrieves the dictionary representation
        """
        if attrs is not None:
            new_dict = {}
            for idx in attrs:
                if idx in self.__dict__:
                    new_dict[idx] = self.__dict__[idx]
            return new_dict
        return self.__dict__

    def reload_from_json(self, json):
        """
        replaces all attributes of Student
        """
        for idx in self.__dict__:
            if idx in json:
                self.__dict__[idx] = json[idx]
