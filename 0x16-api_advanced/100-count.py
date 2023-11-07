#!/usr/bin/python3
""" Count it """

import requests


def count_words(subreddit, word_list, after=None, count_dict=None):
    """
    Recursively retrieve and count keywords in the titles of
    hot posts for a given subreddit using the Reddit API.

    Args:
        subreddit (str): The name of the subreddit.
        word_list (list): A list of keywords to count.
        after (str): The "after" parameter for pagination
        (used in recursive calls).
        count_dict (dict): A dictionary to store the keyword
        counts.

    Returns:
        None
    """
    if not subreddit:
        return

    if count_dict is None:
        count_dict = {}

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "ALX project about advanced API"}

    params = {"limit": 100, "after": after}
    response = requests.get(url, params=params, headers=headers)

    if response.status_code == 200:
        data = response.json().get("data", {})
        posts = data.get("children", [])

        for post in posts:
            title = post["data"]["title"].lower()
            for word in word_list:
                count = title.count(word.lower())
                if word not in count_dict:
                    count_dict[word] = 0
                count_dict[word] += count

        after = data.get("after")
        if after:
            count_words(subreddit, word_list, after, count_dict)
        else:
            sorted_counts = sorted\
                            (count_dict.items(), key=lambda x: (-x[1], x[0]))
            for word, count in sorted_counts:
                if count > 0:
                    print(f"{word}: {count}")
    else:
        return
