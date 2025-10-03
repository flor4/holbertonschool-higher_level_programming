#!/usr/bin/python3

"""The json module allows you to load a JSON
string and convert it into a Python object.
"""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)
