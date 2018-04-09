#!/usr/bin/python3
"""
    Sends a POST request to the URL passed into script
"""
import urllib.request
import urllib.parse
from sys import argv
if __name__ == "__main__":
    data = {'email': argv[2]}
    data = urllib.parse.urlencode(data)
    data = data.encode('ascii')
    url = argv[1]
    req = urllib.request.Request(url, data)
    with urllib.request.urlopen(req) as response:
        email = response.getheader('email')
        print("Your email is: {}".format(email))
