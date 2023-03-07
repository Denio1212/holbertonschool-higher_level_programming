#!/usr/bin/python3
"""
The base class that will be the blueprint
"""
import json


class Base:
    """
    blueprint for classes
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        constructor
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns JSON string of a list of dicts
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the json to a file
        """
        a_list = []
        file = cls.__name__ + '.json'
        if list_objs is not None:
            for idx in list_objs:
                a_list.append(idx.to_dictionary())
        with open(file, mode='w') as f:
            f.write(cls.to_json_string(a_list))

    @staticmethod
    def from_json_string(json_string):
        """
        loads a list from json_strings
        """
        if json_string is not None or json_string != "":
            return json.loads(json_string)

