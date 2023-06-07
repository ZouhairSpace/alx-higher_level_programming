#!/usr/bin/python3
def uppercase(str):
    for char in str:
        char_code = ord(char)
        if char_code >= 97 and char_code <= 122:
            char_code -= 32
        char = chr(char_code)
        print("{}".format(char), end='')
    print("")
