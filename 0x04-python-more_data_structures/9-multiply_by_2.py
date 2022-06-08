#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    dict_ = {}
    for k in a_dictionary:
        dict_[k] = a_dictionary[k] * 2
    return dict_
