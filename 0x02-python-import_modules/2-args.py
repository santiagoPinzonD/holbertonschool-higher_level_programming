#!/usr/bin/python3
def main():
    import sys
    print("{} argument:" .format(len(sys.argv)))
    for x in range(1, len(sys.argv)):
        print("{:d}: {}" .format(x, sys.argv[x]))
if __name__ == '__main__':
    main()
