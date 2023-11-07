#!/usr/bin/python3
"""
prints the titles of the first 10
hot posts listed for a given subreddit

"""
import requests


def top_ten(subreddit):
    """Top ten"""
    url = f"https://www.reddit.com/r/{subreddit}/hot/.json?limit=10"
    headers = {"User-Agent": "MyRedditScraper"}

    response = requests.get(url, params={"limit": 10}, headers=headers)

    if response.status_code == 200:
        posts = response.json().get("data", {}).get("children", [])
        for post in posts:
            print(post["data"]["title"])
    else:
        print("None")
