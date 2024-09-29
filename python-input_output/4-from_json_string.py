#!/usr/bin/python3
"""
    file function for from_json_string
"""
import json


def from_json_string(my_str):
    """
        Returns an object represented by a JSON string
        Arguments:
            my_str: Text to convert
    """
    return json.loads(my_str)