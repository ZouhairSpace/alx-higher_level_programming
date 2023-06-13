#!/usr/bin/python3

def print_matrix_integer(input_matrix=[[]]):
    if input_matrix != [[]]:
        for row in input_matrix:
            for element in row:
                print("{:d}".format(element), end=" " if element != row[-1] else '\n')
    else:
        print()
