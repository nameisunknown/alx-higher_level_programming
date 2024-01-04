#!/usr/bin/python3
for count in range(0, 100):
    if count < 10:
        print("0{}, ".format(count), end="")
    elif count < 99:
        print("{}, ".format(count), end="")
    elif count == 99:
        print("{}".format(count), end="\n")
