#!/usr/bin/python3
"""Recurse it!"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Recursively retrieve and append the titles of all
    hot posts for a given subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.
        hot_list (list): A list to store the titles of hot posts.
        after (str): The "after" parameter for pagination
        (used in recursive calls).

    Returns:
        list: A list containing the titles of all hot
        posts for the subreddit, or None if not found.
    """
    if not subreddit:
        return None

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "ALX project about advanced API"}

    params = {"limit": 100, "after": after}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", {})
        posts = data.get("children", [])
        hot_list.extend([post["data"]["title"] for post in posts])

        after = data.get("after")
        if after:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
