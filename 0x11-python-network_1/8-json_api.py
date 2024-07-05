#!/usr/bin/python3
"""
A Python script that takes in a letter, sends a POST request to
http://0.0.0.0:5000/search_user with the letter as a parameter.
"""
import requests
import sys

if __name__ == "__main__":
    q = sys.argv[1] if len(sys.argv) > 1 else ""
    response = requests.post('http://0.0.0.0:5000/search_user', data={'q': q})
    try:
        json_response = response.json()
        if json_response:
            print(f"[{json_response.get('id')}] {json_response.get('name')}")
        else:
            print("No result")
    except ValueError:
        print("Not a valid JSON")
