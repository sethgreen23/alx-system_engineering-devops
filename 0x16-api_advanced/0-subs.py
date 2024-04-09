#!/usr/bin/python3
"""Total number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """Number of subscribers for certain subredit"""
    headers = {"User-Agent": "ChangeMeClient/0.1 by sethgreen2015"}
    r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                     headers=headers, allow_redirects=False)
    if r.status_code == 200:
        subscribers = r.json().get('data', None).get('subscribers', None)
        if subscribers is None:
            return (0)
        else:
            return (subscribers)
    else:
        return (0)
