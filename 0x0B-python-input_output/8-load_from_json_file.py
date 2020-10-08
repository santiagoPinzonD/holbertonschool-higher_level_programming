#!/usr/bin/python3
"""create"""
import json


def load_from_json_file(filename):
    """create a function"""
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
