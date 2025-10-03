#!/usr/bin/python3
import json
"""Convert a JSON string to a Python object."""


def from_json_string(my_str):
    """Convert a JSON string to a Python object."""
    return json.loads(my_str)
