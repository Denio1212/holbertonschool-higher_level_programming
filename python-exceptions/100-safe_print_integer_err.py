#!/usr/bin/python3
import sys


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return True
    except ValueError as err1:
        print("Exception: {}".format(err1), file=sys.stderr)
        return False
    except TypeError as err2:
        print("Exception: {}".format(err2), file=sys.stderr)
        return False
