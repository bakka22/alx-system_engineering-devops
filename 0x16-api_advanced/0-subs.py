#!/usr/bin/python3
""" queries the Reddit API and returns the number of subscribers """


import requests


def number_of_subscribers(subreddit):
    """ queries the Reddit API and returns the number of subscribers """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {"User-Agent": "Python Reddit API Client"}
    response = requests.get(url, allow_redirects=False, headers=headers)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data.get('data').get('subscribers')
