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

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if "data" in data and "children" in data["data"]:
            posts = data["data"]["children"]
            if len(posts) == 0:
                print("No posts found in this subreddit.")
            else:
                for i, post in enumerate(posts):
                    print(f"{i + 1}: {post['data']['title']}")
        else:
            print("None")
