#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for list_ in my_list:
        if list_ == search:
            copy.append(replace)
        else:
            copy.append(list_)
    return copy
