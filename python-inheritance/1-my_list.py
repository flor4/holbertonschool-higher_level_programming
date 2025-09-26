#!/usr/bin/python3
"""
Defines the MyList class inheriting from list.
"""


class MyList(list):
    """
    Class that inherits from list and adds a method to print the sorted list.
    """

    def print_sorted(self):
        """
        Prints the list in ascending sorted order without modifying it.
        """
        print(sorted(self))
