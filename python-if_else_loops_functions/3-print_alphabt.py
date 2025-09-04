#!/usr/bin/python3

for letter in range(97, 123):
    if chr(letter) in ('q', 'e'):
        continue
    print("{}".format(chr(letter)), end="")
