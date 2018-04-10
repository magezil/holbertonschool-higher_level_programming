#!/usr/bin/python3
"""
    Takes two arguments to send a request to the Github API to get 10 commits
    Arguments should be [repository name, owner name]
"""
if __name__ == "__main__":
    import requests
    from sys import argv
    repo = argv[1]
    owner = argv[2]
    r = requests.get('https://api.github.com/repos/{}/{}/commits'
                     .format(owner, repo)).json()
    count = 0
    for line in r:
        print("{}: {}".format(line.get("sha"),
              line.get("commit").get("author").get("name")))
        count += 1
        if count == 10:
            break
