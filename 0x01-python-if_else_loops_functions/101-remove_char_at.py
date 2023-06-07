#!/usr/bin/python3
def remove_char_at(string, n):
    if n < 0:
        return string
    count = 0
    string_copy = ""
    for element in string:
        if count == n:
            count += 1
            continue
        string_copy += string[count]
        count += 1
    return string_copy
