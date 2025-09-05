#!/usr/bin/python3

import sys

if __name__ == "__main__":
    args = sys.argv[1:]
    count = len(args)

    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
    else:
        print(f"{count} arguments:")

    i = 1
    for arg in args:
        print(f"{i}: {arg}")
        i += 1
