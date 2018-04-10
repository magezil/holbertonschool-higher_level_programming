#!/usr/bin/python3
"""
    Send a search request to the Twitter API for given string
    Format: [<Tweet ID>] <Tweet text> by <Tweet owner name>
"""
import requests
from base64 import b64encode
from sys import argv
if __name__ == "__main__":
    key = b64encode(argv[1].encode())
    secret = b64encode(argv[2].encode())
    token = b64encode("{}:{}".format(key, secret).encode())
    search = argv[3]
    r = requests.post('https://api.twitter.com/oauth2/token', headers={'Authorization': "Basic {}".format(token), 'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'}, data={'grant_type': 'client_credentials'})
    access_token = r.json().get("access_token")
    r = requests.get('https://api.twitter.com/1.1/search/tweets.json', headers = {"Authorization": "Bearer {}".format(access_token)}, params={"q": search, "count": 5})
    for post in r.json():
        print("[{}] {} by {}".format(post.get("id"), post.get("text"), post.get("user").get("name")))
