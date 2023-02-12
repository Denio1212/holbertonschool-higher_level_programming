#!/usr/bin/python3
"""
Appending into file
"""


def append_write(filename="", text=""):
    """
    The function to append at EOF
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
