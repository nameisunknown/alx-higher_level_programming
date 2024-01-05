#!/usr/bin/python3
import sys

if __name__ == "__main__":
    collected = sys.argv
    lenofcoll = len(collected)
    count = 1
    sum = 0
    while count < lenofcoll:
        sum = sum + eval(collected[count])
        count = count + 1
    print("{}".format(sum), end="\n")
