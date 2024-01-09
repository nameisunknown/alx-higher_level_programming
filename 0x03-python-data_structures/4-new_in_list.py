#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    listcp = my_list
    if idx < 0:
        return listcp
    elif idx > (len(listcp) - 1):
        return listcp
    else:
        listcp[idx] = element
        return listcp
