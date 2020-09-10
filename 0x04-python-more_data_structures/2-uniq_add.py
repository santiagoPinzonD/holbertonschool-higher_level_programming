#!/usr/bin/python3
def uniq_add(my_list=[]):
    mylist = set(my_list)
    suma = 0
    for x in mylist:
        suma += x
    return suma
