#!/usr/bin/python3
"""
    Search for people in Star Wars API and account for pagination
"""
import requests
from sys import argv
if __name__ == "__main__":
    params = {"search": argv[1] if len(argv) > 1 else ""}
    try:
        url = 'https://swapi.co/api/people/'
        r = requests.get(url, params=params).json()
        count = r.get("count")
        print("Number of results: {}".format(count))
        if count > 0:
            while r:
                for res in r.get("results"):
                    print(res["name"])
                next_page = requests.get(r.get("next"))
                r = next_page.json()
    except ValueError:
        pass
