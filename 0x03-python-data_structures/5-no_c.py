#!/usr/bin/env python3
def no_c(my_string):
    s = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            s += x
    return s
