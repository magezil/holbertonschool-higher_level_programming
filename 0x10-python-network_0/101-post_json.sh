#!/bin/bash
# Sends a JSON POST request to URL and displays the body of the response
curl -s "$1" -X POST -H "Content-Type: application/json" -d @"$2"
