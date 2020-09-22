#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    _newlist = []
    for x in range(0, list_length):
        try:
            s = 0
            s = my_list_1[x]/my_list_2[x]
        except (TypeError, ValueError):
            print("wrong type")
        except ZeroDivisionError:
            print("division by 0")
        except IndexError:
            print("out of range")
        finally:
            _newlist.append(s)
    return _newlist
