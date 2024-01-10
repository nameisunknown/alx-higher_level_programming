#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    if idx < 0:
        return my_list
    else:
        count = 0
        newl = []
        while count < len(my_list):
            if count != idx:
                newl.append(my_list[count])
            count += 1
        del my_list[idx]
        return newl
