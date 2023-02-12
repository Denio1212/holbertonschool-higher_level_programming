#!/usr/bin/python3
"""
Writes to a txt file and returns the characters written
"""


def write_file(filename="", text=""):
    """
    writer online
    """
    with open(filename, mode='w', encoding='utf-8') as f:
        return f.write(text)
