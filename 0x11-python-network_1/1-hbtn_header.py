#!/usr/bin/python3
"""
    Script sends a request to given URL
    Displays value of X-Request-Id variable from header of response
"""
import urllib.request
from sys import argv
url = argv[1]
req = urllib.request.Request(url)
with urllib.request.urlopen(req) as response:
    print(response.getheader('X-Request-Id'))
