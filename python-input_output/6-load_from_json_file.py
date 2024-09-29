#!/usr/bin/python3
"""
    file function for load_from_json_file
"""
import json


def load_from_json_file(filename):
    """
    Creates an Object from a JSON file.

    Arguments:
        filename: The name of the file containing the JSON string.
    """
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
