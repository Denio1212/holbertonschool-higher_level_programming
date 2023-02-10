#!/usr/bin/python
"""
Making inheritance
"""


class MyList(list):
    """
    Inheritant
    """
    def print_sorted(self):
        """
        Prints the sorted list
        """
        print(sorted(self))

