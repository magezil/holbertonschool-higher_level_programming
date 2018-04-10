#!/usr/bin/python3
"""
    Takes two arguments to send a request to the Github API to get 10 commits
    Arguments should be [repository name, owner name]
"""
import requests
from sys import argv
repo = argv[1]
owner = argv[2]
r = requests.get('https://api.github.com/repos/{}/{}/commits'.format(owner, repo)).json()
for i in range(10):
    print("{}: {}".format(r[i]["sha"], r[i]["commit"]["author"]["name"]))
