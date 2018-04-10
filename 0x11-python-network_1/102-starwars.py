#!/usr/bin/python3
"""
    Build on previous search to include list of films person is in
"""
import requests
from sys import argv, exit
if __name__ == "__main__":
    params = {"search": argv[1] if len(argv) > 1 else ""}
    try:
        url = 'https://swapi.co/api/people/'
        r = requests.get(url, params=params).json()
        count = r.get("count")
        print("Number of results: {}".format(count))
        if count == 0:
            exit()
        while r:
            for res in r.get("results"):
                print(res["name"])
                films = res.get("films")
                for f in films:
                    print("\t{}".format(requests.get(f).json().get("title")))
            next_page = requests.get(r.get("next"))
            r = next_page.json()
    except ValueError:
        pass
