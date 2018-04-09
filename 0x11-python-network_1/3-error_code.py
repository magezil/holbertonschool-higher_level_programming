#!/usr/bin/python3
"""
    Print error code in utf-8
"""
import urllib.request
import urllib.parse
from urllib.error import URLError, HTTPError
from sys import argv
if __name__ == "__main__":
    req = urllib.request.Request(argv[1])
    try:
        with urllib.request.urlopen(req) as response:
            print(response.read().decode(encoding="utf-8"))
    except URLError as e:
        print("Error code: {}".format(e.code))
