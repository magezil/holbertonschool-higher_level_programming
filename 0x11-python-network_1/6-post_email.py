#!/usr/bin/python3
"""
    Sends a POST request to passed URL with email as parameter and
    displays body of response
"""
import requests
from sys import argv
if __name__ == "__main__":
    r = requests.post(argv[1], {'email': argv[2]})
    print(r.text)
