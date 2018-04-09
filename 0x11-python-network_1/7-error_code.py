#!/usr/bin/python3
"""
    Send request to given URL and display body of response
"""
import requests
from sys import argv
if __name__ == "__main__":
    r = requests.get(argv[1])
    code = r.status_code
    if code > 400:
        print("Error code: {}".format(code))
    else:
        print(r.text)
