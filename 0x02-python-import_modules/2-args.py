#!/usr/bin/python3

if __name__ == "__main__":
    import sys
    cmdsys = sys.argv
    count = 1
    if (len(cmdsys) == 1):
        print("0 arguments.")
    elif (len(cmdsys) == 2):
        print("1 argument:", end="\n")
        print("1: {}".format(cmdsys[1])) 
    else:
        while count < len(cmdsys):
            print("{} arguments:".format(len(cmdsys)))
            print("{}: {}".format(count, cmdsys[count]))
            count = count + 1
