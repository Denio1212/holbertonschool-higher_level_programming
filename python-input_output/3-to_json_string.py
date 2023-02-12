#!/usr/bin/python3
"""
Converter to JSON
"""
import json


def to_json_string(my_obj):
    """
    Func to convert
    """
    return json.dumps(my_obj, ensure_ascii=False)
