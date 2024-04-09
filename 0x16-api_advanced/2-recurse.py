#!/usr/bin/python3
"""hot posts for reddit recursivaley"""
import requests


def recurse(subreddit, hot_list=[], after='after'):
    """hot posts for reddit recursivaley."""

    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    if after != 'after':
        url = url + f'?after={after}'

    headers = requests.utils.default_headers()
    headers['User-Agent'] = 'My User Agent 0.0.1'

    res = requests.get(url, headers=headers, allow_redirects=False)
    if res.status_code != 200:
        return None
    resp = res.json().get('data', {}).get('children', None)

    for r in resp:
        hot_list.append(r.get('data').get('title'))
    after = res.json().get('data').get('after')

    if not after:
        return hot_list
    return (recurse(subreddit, hot_list, after))
