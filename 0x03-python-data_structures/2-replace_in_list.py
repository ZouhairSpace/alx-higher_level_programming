#!/usr/bin/python3

def replace_in_list(my_list, index, new_element):
    list_length = len(my_list)
    if index < 0:
        return my_list
    elif index > list_length - 1:
        return my_list
    else:
        my_list[index] = new_element
        return my_list

