#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    number_count = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
        except IndexError:
            break
        number_count += 1
    print()
    return number_count
