#!/usr/bin/python3
import string
asc = string.ascii_lowercase
for ac in asc:
    if ac != 'q' and ac != 'e':
        print("{}".format(ac), end="")
