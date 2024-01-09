#!/usr/bin/python3

def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    elif len(my_list) == 1:
        return my_list[0]
    else:
        counter = 0
        swap = 0
        while counter < len(my_list):
            if swap > my_list[counter]:
                swap = swap
            else:
                swap = my_list[counter]
            counter += 1
        return swap 
