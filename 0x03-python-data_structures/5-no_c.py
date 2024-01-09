#!/usr/bin/python3

def no_c(my_string):
    newstr = ""
    length = len(my_string)
    count = 0
    while count < length:
        if not my_string[count] == 'c' and not my_string[count] == 'C':
            newstr = newstr + my_string[count]
        count = count + 1
    return newstr
