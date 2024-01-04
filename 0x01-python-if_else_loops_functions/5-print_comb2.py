#!/usr/bin/python3
for count in range(0, 100):
    if count < 99:
        print("{:02}, ".format(count), end="")
    elif count == 99:
        print("{}".format(count), end="\n")
