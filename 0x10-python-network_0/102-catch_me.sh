#!/bin/bash
# Get the server to respond with "You got me!" by sending a request with curl to 0:5000/catch_me
curl -sL 0:5000/catch_me -X PUT "You got me!" -H "Origin: HolbertonSchool" -d "user_id=98"
