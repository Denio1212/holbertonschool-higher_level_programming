#!/usr/bin/python3
"""
A funct to read and print a file
"""


def read_file(filename=""):
    """
    reads a file and prints the stuff
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
