#!/usr/bin/python3

def uppercase(str):
    for char in str:
        if 'a' <= char <= 'z':
            char = chr(ord(char) - 32)
            """
            ascii_code = ord(char)
            uppercase_code = ascii_code - 32
            char = chr(uppercase_code)
            """
        print("{}".format(char), end="")
    print()
