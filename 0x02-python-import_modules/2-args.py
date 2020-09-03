#!/usr/bin/python3
def main():
    import sys
    if len(sys.argv) == 1:
        print("0 arguments.")
    if len(sys.argv) == 2:
        print("1 argument:")
    if len(sys.argv) > 2:
        print("{} arguments:" .format(len(sys.argv) - 1))
    for x in range(1, len(sys.argv)):
        print("{:d}: {}" .format(x, sys.argv[x]))
if __name__ == '__main__':
    main()
