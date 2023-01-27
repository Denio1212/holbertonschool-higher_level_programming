#!/usr/bin/python3

def roman_to_int(roman_string):
    result = 0
    romannum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    if type(roman_string) == str:
        for i in roman_string:
            if i in romannum:
                result += romannum[i]
                continue

    return result       
