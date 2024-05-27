#!/usr/bin/python3
"""
    file for save_to_json_file function
"""
import json


def save_to_json_file(my_obj, filename):
    """
        writes an Object to a text file, using a JSON representation
        Arguments:
            my_obj: Object
            filename: Text to write
    """
    with open(filename, "w+") as f:
        f.write(json.dumps(my_obj))
