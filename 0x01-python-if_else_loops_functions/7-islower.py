#!/usr/bin/python3
def islower(c):
    character_code = ord(c)
    if character_code >= 97 and character_code <= 122:
        return True
    else:
        return False
