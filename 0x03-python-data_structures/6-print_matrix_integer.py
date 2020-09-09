#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if(matrix == [[]]):
        print("")
    else:
        for i in matrix:
            z = 0
            for x in i:
                if z >= len(i) - 1:
                    print("{:d}".format(x), end="")
                else:
                    print("{:d}".format(x), end=" ")
                z = z + 1
            print("")
