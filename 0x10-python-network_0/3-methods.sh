#!/bin/bash
# Displays all HTTP methods server can accept
curl -sI "$1" | grep "Allow" | cut -d" " -f 2-
