#!/usr/bin/python3


def text_indentation(text):
    if type(text) is not str:
        raise TypeError("text must be a string")
    delimiter = {'.', '?', ':'}
    txt = ''

    for s in text:
        txt += s
        if s in delimiter:
            print(txt.strip())
            print()
            txt = ''
    print(txt.strip(), end='')
