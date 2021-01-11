#!/usr/bin/python3
""" script that takes in a URL, sends a request to the
URL and displays the value of the X-Request-Id
"""

if __name__ == "__main__":
    url = sys.argv[1]
    with urlopen(url) as response:
        req = response.info()
        print(req['X-Request-Id'])
