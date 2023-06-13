#!/usr/bin/python3

def no_c(input_string):
    result = []
    for char in input_string:
        if char != 'c' and char != 'C':
            result.append(char)
    return ''.join(result)
