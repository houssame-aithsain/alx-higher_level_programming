#!/usr/bin/python3
"""
A Python script that takes GitHub credentials
(username and personal access token)
and uses the GitHub API to display the user's id.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    token = sys.argv[2]
    url = 'https://api.github.com/user'
    response = requests.get(url, auth=(username, token))
    try:
        print(response.json().get('id'))
    except ValueError:
        print("None")
