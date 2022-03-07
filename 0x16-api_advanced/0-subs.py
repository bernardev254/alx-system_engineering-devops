#!/usr/bin/python3
"""api query module"""


def number_of_subscribers(subreddit):
    """queries Reddit Api returning subscribers no"""
    import requests

    data_dict = requests.get('https://www.reddit.com/r/{}/about.json'
                             .format(subreddit),
                             headers={'User-Agent': 'User-Agent'},
                             allow_redirects=False)
    if data_dict.status_code >= 300:
        return 0

    sub = data_dict.json().get('data').get('subscribers')
    return sub
