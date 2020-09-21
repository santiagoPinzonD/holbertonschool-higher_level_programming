#!/usr/bin/python3
def safe_print_division(a, b):
    while True:
        try:
            result = a / b
            return result
            break
        except ZeroDivisionError:
            result = None
        finally:
            print("Inside result: {}" .format(result))
            return result
