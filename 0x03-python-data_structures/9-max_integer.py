#!/usr/bin/python3
def max_integer(my_list=[]):
    if (len(my_list) == 0):
        return None
    maxx = my_list[0]
    for x in my_list:
        if(x > maxx):
            maxx = x
    return maxx
