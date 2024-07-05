#!/bin/bash
# Sends a POST request with email and subject parameters and displays the response body
curl -sX POST -d "email=test@gmail.com&subject=I%20will%20always%20be%20here%20for%20PLD" "$1"
