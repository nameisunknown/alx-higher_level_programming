#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    cmdsys = sys.argv
    count = 1
    while count < len(cmdsys):
        print("{}: {}".format(count, sys.argv[count]))
        count = count + 1
