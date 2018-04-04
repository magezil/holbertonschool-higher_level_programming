#!/bin/bash
# Use curl options to get status code of response
curl -s "$1" -o /dev/null -w "%{http_code}"
