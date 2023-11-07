#!/usr/bin/python3
"""module 1-top_ten"""
import requests
import json


def top_ten(subreddit):
    """function that queries the Reddit API and returns
    the titles of the first 10 hot posts listed for a given subreddit
    """

    url = f"https://www.reddit.com/r/{subreddit}/hot/.json"
    headers = {"User-Agent": "linux:0x16.api.advanced/1.0"}
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return None
    data = json.loads(response.text)
    i = 0
    for i, elmt in enumerate(data['data']['children'][:10]):
        print(elmt['data']['title'])
