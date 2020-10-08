#!/usr/bin/python3
"""create"""
import json


def save_to_json_file(my_obj, filename):
    """create a function"""
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
