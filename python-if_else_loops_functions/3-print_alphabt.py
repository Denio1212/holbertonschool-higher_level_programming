#!/usr/bin/python3
for c in range(ord('a'), ord('z') + 1):
    if chr(c) not in ['e', 'q']:
        print("{:s}".format(chr(c)), end='')
