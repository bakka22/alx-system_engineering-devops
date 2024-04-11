#!/usr/bin/python3
""" prints the titles of the first 10 hot posts listed for a given
    subreddit """


import requests


def top_ten(subreddit):
    """ prints the titles of the first 10 hot posts listed for a given
    subreddit """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Python Reddit API Client"}
    params = {
            "limit": 9,
    }
    response = requests.get(url, allow_redirects=False, headers=headers,
                            params=params)
    if response.status_code != 200:
        print(None)
        return
    data = response.json()
    hot = data.get('data').get('children')
    for post in hot:
        print(post.get('data').get('title'))
