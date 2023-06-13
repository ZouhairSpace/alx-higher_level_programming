#!/usr/bin/python3

def print_reversed_list_integer(new_list=[]):
    if not new_list:
        return None
    new_list.reverse()
    for num in new_list:
        print('{:d}'.format(num))
