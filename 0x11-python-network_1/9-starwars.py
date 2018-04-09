#!/usr/bin/python3
"""
    Send search request to Star Wars API with given string
"""
import requests
from sys import argv
if __name__ == "__main__":
    params = {"search": argv[1] if len(argv) > 1 else ""}
    try:
        r = requests.get('https://swapi.co/api/people/', params=params).json()
        count = r.get("count")
        print("Number of results: {}".format(count))
        if count > 0:
            for res in r.get("results"):
                print(res["name"])
    except ValueError:
        print("Not a valid JSON")
