#!/usr/bin/python3
def islower(c):
    for x in range(97, 122):
        if ord(c) == x:
            return True
    return False
