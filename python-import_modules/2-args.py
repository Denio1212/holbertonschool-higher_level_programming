#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    argument = len(argv) - 1
    if argument == 1:
        print("{} argument:".format(argument))
    elif argument == 0:
        print("{} arguments.".format(argument))
    else:
        print("{} arguments:".format(argument))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
