#!/usr/bin/python3
"""Top 10 hot posts in subredit."""
import requests


def top_ten(subreddit):
    """Top 10 hot posts in subredit."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"

    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'My User Agent 0.0.1'

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        print('None')
    else:
        top_ten = res.json().get('data', {}).get('children')
        for top in top_ten:
            print(top.get('data').get('title'))
