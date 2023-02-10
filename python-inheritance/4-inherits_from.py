#!/usr/bin/python3
"""
Returns true only if subclass
"""


def inherits_from(obj, a_class):
    """
    simple return value
    """
    return isinstance(obj, a_class) and type(obj) is not a_class