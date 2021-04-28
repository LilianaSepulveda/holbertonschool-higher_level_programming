#!/usr/bin/python3
import sys
if __name__ == "__main__":

    count = len(sys.argv) - 1
    if count == 0:
        print("{} argunments.".format(count))
    elif count == 1:
        print("{} argunment:".format(count))
    else:
        print("{} arguments:".format(count))
    for index in range(len(0, count)):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
