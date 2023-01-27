#!/usr/bin/python3

def roman_to_int(roman_string):
    romannum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if isinstance(roman_string, str):
        for i in romanstr:
            if i in romannum:
               if i == I:
                    i += i + 1
                    continue
                elif i == V:
                    i += i + 5
                    continue
                elif i == X:
                    i += i + 10
                    continue
                elif i == L:
                    i += i + 50
                    continue
                elif i == C:
                    i += i + 100
                    continue
                elif i == D:
                    i += i + 500
                    continue
                elif i == M:
                    i += i + 1000
                    continue
            else:
               return 0
    else:
        return 0
    return i



