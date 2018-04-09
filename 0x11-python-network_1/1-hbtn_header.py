#!/usr/bin/python3
"""
    Script sends a request to given URL
    Displays value of X-Request-Id variable from header of response
"""
import urllib.request
import sys
with urllib.request.urlopen(sys.argv[1]) as response:
    print(response.getheader('X-Request-Id'))
