#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    suma = 0
    try:
        for z in range(0, x):
            if type(my_list[z]) is int:
                print("{:d}" .format(my_list[z]), end="")
                suma += 1
        print()
        return suma
    except (TypeError, ValueError):
        print()
        return z
