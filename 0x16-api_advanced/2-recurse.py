#!/usr/bin/python3
"""api query module"""


def recurse(subreddit, hot_list=[], count=0, after=None):
    """queries Reddit Api recursefully returning all hot
    tittles for a subreddit"""
    import requests

    data_dict = requests.get('https://www.reddit.com/r/{}/hot.json'
                             .format(subreddit),
                             headers={'User-Agent': 'User-Agent'},
                             params={'count': count, 'after': after},
                             allow_redirects=False)
    if data_dict.status_code >= 300:
        return None
    hots = data_dict.json().get('data').get('children')
    for hot in hots:
        tittle = hot.get('data').get('title').encode('ascii', 'ignore')\
            .decode('ascii')
        hot_list.append(tittle)
    if not data_dict.json().get('data').get('after'):
        return hot_list

    return recurse(subreddit, hot_list, data_dict.json().get('data')
                   .get('count'), data_dict.json().get('data').get('after'))
