#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    suma = 0
    for z in range(x):
        try:
            print("{:d}".format(my_list[z]), end="")
            suma += 1
        except (TypeError, ValueError):
            pass
    print()
    return suma
