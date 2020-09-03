#!/usr/bin/python3
def main():
    import sys
    suma = 0
    for x in range(1, len(sys.argv)):
        suma += int(sys.argv[x])
    print(suma)
if __name__ == '__main__':
    main()
