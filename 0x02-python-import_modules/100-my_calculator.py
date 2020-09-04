#!/usr/bin/python3
def main():
    from calculator_1 import add, sub, mul, div
    import sys
    av = sys.argv
    a = int(av[1])
    b = int(av[3])
    if len(av) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    if av[2] == "+":
        print("{} + {} = {}".format(a, b, add(a, b)))
    elif av[2] == "-":
        print("{} - {} = {}".format(a, b, sub(a, b)))
    elif av[2] == "/":
        print("{} / {} = {}".format(a, b, div(a, b)))
    elif av[2] == "*":
        print("{} * {} = {}".format(a, b, mul(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)
if __name__ == "__main__":
    main()
