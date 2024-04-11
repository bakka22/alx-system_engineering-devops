#!/usr/bin/python3
"""  returns a list containing the titles of all hot articles for a
given subreddit """


import requests


def recurse(subreddit, hot_list=[], after=None):
    """  returns a list containing the titles of all hot articles for
    a given subreddit"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {"User-Agent": "Python Reddit API Client"}
    if after:
        params = {
                "limit": 100,
                "after": after
        }
    else:
        params = {
               "limit": 100,
        }
    response = requests.get(url, allow_redirects=False, headers=headers,
                            params=params)
    if response.status_code != 200:
        return None
    data = response.json()
    after = data.get('data').get('after')
    hot = data.get('data').get('children')
    for post in hot:
        hot_list.append(post.get('data').get('title'))
    if after is None:
        return hot_list
    recurse(subreddit, hot_list, after)
    return hot_list
