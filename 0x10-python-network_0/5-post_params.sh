#!/bin/bash
# send a POST request to a given URL
curl -s -X POST -d "email=hr@holbertonschool.com&subject=I will always be here for PLD" "$1"
