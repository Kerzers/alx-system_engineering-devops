#!/usr/bin/python3
"""module 0-subs"""
import requests
import json


def number_of_subscribers(subreddit):
    """function that queries the Reddit API and returns the number
    of subscribers for a given subreddit"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {"User-Agent": "linux:0x16.api.advanced/1.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return 0
    data = json.loads(response.text)
    return data['data']['subscribers']
