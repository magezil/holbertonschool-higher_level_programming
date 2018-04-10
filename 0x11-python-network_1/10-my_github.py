#!/usr/bin/python3
"""
    Script takes Github credentials (username and password) and uses the
    Github API to display id
"""
import requests
from sys import argv
if __name__ == "__main__":
    username = argv[1]
    password = argv[2]
    r = requests.get('https://api.github.com/user',
                     params={"login": username},
                     auth=(username, password)).json()
    if "id" in r:
        print(r["id"])
    else:
        print(None)
