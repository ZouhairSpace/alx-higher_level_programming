#!/usr/bin/python3

def multiple_returns(sentence):
    if len(sentence) == 0:
        result_tuple = len(sentence), None
        return result_tuple
    result_tuple = len(sentence), sentence[0]
    return result_tuple
