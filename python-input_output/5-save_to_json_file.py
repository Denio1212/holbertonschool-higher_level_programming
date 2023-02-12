#!/usr/bin/python3
"""
Writes an object to a file using JSONe
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Up Top
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
