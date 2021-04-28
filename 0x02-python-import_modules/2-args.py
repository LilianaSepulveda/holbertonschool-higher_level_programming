#!/usr/bin/python3
if __name__ == "__main__":
    """Print number and list of arguments."""
    import sys

    count = len(sys.argv) - 1
    if count == 0:
        print("0 argunments.")
    elif count == 1:
        print("1 argunment:")
    else:
        print("{} arguments:".format(count))
    for index in range(count):
        print("{}: {}".format(index + 1, sys.argv[index + 1]))
