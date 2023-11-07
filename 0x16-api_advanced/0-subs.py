#!/usr/bin/python3
"""How many subs"""

import requests


def number_of_subscribers(subreddit):
    """represents the Reddit API URL"""
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "number_of_subscribers"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        subscribers = data["data"]["subscribers"]
        return subscribers
    else:
        return 0
