#!/usr/bin/python3
"""
    Script sends a request to given URL
    Displays value of X-Request-Id variable from header of response
"""
import urllib.request
from sys import argv
url = argv[1]
local_file, headers = urllib.request.urlretrieve(url)
for h in headers._headers:
    if h[0] == 'X-Request-Id':
        print(h[1])
