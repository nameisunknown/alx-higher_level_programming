#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    count = 0
    while count < len(my_list):
        if (my_list[count] % 2) == 1:
            new_list.append(False)
        elif (my_list[count] % 2) == 0:
            new_list.append(True)
        count += 1
    return new_list
