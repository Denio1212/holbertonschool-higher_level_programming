#!use/bin/python3
"""
Creates an object from JSON
"""
import json


def load_from_json_file(filename):
    """
    Makes a new obj from json
    """
    with open(filename) as f:
        return json.load(f)
