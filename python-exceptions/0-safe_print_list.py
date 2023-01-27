#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    num_count = 0
    for i in range(x):
        try:
            print(my_list[i], end='')
        except IndexError:
            break
        num_count += 1
    print()
    return num_count
