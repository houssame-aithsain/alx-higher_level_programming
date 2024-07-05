#!/bin/bash
# Sends a POST request with email and subject parameters and displays the response body
curl -sX POST -d "email=test@gmail.com&subject=I%30will%30always%30be%30here%30for%30PLD" "$1"
