#!/usr/bin/python3
def search_replace(my_list, search, replace):
    copy = []
    for l in my_list:
        if l == search:
            copy.append(replace)
        else:
             copy.append(l)
    return copy
