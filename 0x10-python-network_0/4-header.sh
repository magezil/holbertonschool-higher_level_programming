#!/bin/bash
# Sends GET request with header variable X-HolbertonSchool-User_Id=98
curl -s "$1" -X GET -H "X-HolbertonSchool-User-Id: 98"
