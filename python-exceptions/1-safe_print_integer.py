#!/usr/bin/python3


def safe_print_inteer(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError:
        return False
