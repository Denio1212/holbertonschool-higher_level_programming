#!/usr/bin/python3


if __name__ == "__main__":
    from sys import argv
    arguments = len(argv)
    summary = 0
    for arg in range(1, arguments):
        summary += int(argv[arg])
    print("{}".format(summary))
