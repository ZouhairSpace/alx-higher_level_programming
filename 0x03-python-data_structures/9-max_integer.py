#!/usr/bin/python3

def max_integer(input_list=[]):
    if input_list is None or len(input_list) == 0:
        return None
    largest = input_list[0]
    for num in input_list:
        if num > largest:
            largest = num
    return largest
