#!/usr/bin/python3

def delete_at(input_list=[], index=0):
    if index >= 0 and index < len(input_list):
        del input_list[index]
    return input_list
