#!/usr/bin/python3
"""Number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    """
        Number of subscribers
    """
    url = f"https://www.reddit.com/r/{subreddit}/about.json"

    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'My User Agent 0.0.1'

    res = requests.get(url, headers=headers, allow_redirects=False).json()
    subscribers = res.get('data', {}).get('subscribers')
    if not subscribers:
        return 0
    return subscribers
