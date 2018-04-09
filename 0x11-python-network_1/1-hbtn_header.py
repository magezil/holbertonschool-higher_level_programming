#!/usr/bin/python3
"""
    Script sends a request to given URL
    Displays value of X-Request-Id variable from header of response
"""
import urllib.request
import sys
if __name__ == "__main__":
    with urllib.request.urlopen(sys.argv[1]) as response:
        print(response.getheader('X-Request-Id'))
