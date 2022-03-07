#!/usr/bin/python3
"""api query module"""


def top_ten(subreddit):
    """queries Reddit Api returning top 10 posts"""
    import requests

    data_dict = requests.get('https://www.reddit.com/r/{}/hot.json?limit=10'
                             .format(subreddit),
                             headers={'User-Agent': 'User-Agent'},
                             allow_redirects=False)
    if data_dict.status_code >= 300:
        print(None)
    else:
        posts = data_dict.json().get('data').get('children')
        for post in posts:
            print(post.get('data').get('title'))
