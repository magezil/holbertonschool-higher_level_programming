#!/bin/bash
# Send POST request with variable email="hr@holbertonschool.com" and subject="I will always be here for PLD"
curl -s "$1" -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD"
