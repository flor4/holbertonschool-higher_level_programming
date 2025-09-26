#!/usr/bin/env python3
"""
Module defining CountedIterator, which wraps an iterator
and counts how many items have been iterated.
"""


class CountedIterator:
    """
    Custom iterator that counts how many items have been fetched.
    """

    def __init__(self, iterable):
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        item = next(self.iterator)  # May raise StopIteration
        self.count += 1
        return item

    def get_count(self):
        """
        Returns the number of items that have been iterated.
        """
        return self.count
