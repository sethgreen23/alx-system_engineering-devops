#!/usr/bin/python3
"""Total number of subscribers"""


def number_of_subscribers(subreddit):
    """Number of subscribers for certain subredit"""
    import requests
    headers = {"User-Agent": "ChangeMeClient/0.1 by sethgreen2015"}
    r = requests.get(f'https://www.reddit.com/r/{subreddit}/about.json',
                     headers=headers, allow_redirects=False)
    if r.status_code == 200:
        subscribers = r.json().get('data').get('subscribers')
        if subscribers is None:
            return (0)
        else:
            return (subscribers)
    else:
        return (0)
