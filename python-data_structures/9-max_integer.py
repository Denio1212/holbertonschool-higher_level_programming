#!/usr/bin/python3


def max_integer(my_list=[]):
    if list == '':
        return None
    max_num = None
    for number in my_list:
        if max_num is None or max_num < number:
            max_num = number
    return max_num
