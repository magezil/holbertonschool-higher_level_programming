#!/usr/bin/python3
"""
    Sends request to given URL and display value of X-Request-Id in header
"""
import requests
from sys import argv
if __name__ == "__main__":
    r = requests.get(argv[1])
    print(r.headers.get('X-Request-Id'))
