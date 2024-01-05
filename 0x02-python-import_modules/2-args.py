#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    cmdsys = sys.argv

    if (len(cmdsys) == 1):
        print("0 arguments.")
    elif (len(cmdsys) == 2):
        print("1 argument:", end="\n")
        print("1: {}".format(cmdsys[1]))
    else:
        count = 1
        lenght = len(cmdsys) - 1
        print("{} arguments:".format(lenght))
        while count < len(cmdsys):
            print("{}: {}".format(count, cmdsys[count]))
            count = count + 1
