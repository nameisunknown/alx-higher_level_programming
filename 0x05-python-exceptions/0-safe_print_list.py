#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    len_of_list = 0
    counter = 0
    returned_list = []
    try:
        for i in my_list:
            len_of_list = len_of_list + 1
        if x <= len_of_list:
            while counter < x:
                returned_list.append(my_list[counter])
                print(returned_list[counter], end="")
                counter = counter + 1
            print()
            return counter
        else:
            return counter
    except(IndexError, TypeError):
        pass
    return counter
