#!/usr/bin/python3

def roman_to_int(roman_string):
    result = 0
    romannum = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    large = 1
    if type(roman_string) == str:
        for i in roman_string[::-1]:
            if i in romannum:
                if romannum[i] >= large:
                    result += romannum[i]
                    large = romannum[i]
                else:
                    result -= romannum[i]

    return result       
