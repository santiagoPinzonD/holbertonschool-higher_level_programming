#!/usr/bin/python3
def main():
    import hidden_4
    for x in dir(hidden_4):
        if "__" not in x:
            print(x)
if __name__ == '__main__':
    main()
