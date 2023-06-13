#!/usr/bin/python3

def replace_in_list(input_list, index, element):
    size = len(input_list)
    if index < 0:
        return input_list
    elif index > size - 1:
        return input_list
    else:
        input_list[index] = element
        return input_list
