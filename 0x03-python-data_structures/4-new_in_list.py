#!/usr/bin/python3

def new_in_list(my_list, index, new_element):
    list_length = len(my_list)
    list_copy = my_list.copy()
    if index < 0:
        return list_copy
    elif index > list_length - 1:
        return list_copy
    else:
        list_copy[index] = new_element
        return list_copy
