#!/usr/bin/env python3
# encoding: utf-8

"""
"""

import requests


class Reddit:
    """Custom wrapper for the Reddit API
    """

    base_url = 'https://www.reddit.com'

    def __init__(self, username, password, client_id, client_secret, user_agent):
        response = requests.post("https://www.reddit.com/api/v1/access_token", 
                                 auth=requests.auth.HTTPBasicAuth(client_id, client_secret),
                                 data= {"grant_type": "password",
                                        "username": username,
                                        "password": password}, 
                                 headers={'User-Agent': user_agent}).json()
        self.headers : {'User-Agent': user_agent,
                        'Authorization': f'bearer {response["access_token"]}'}

    


class Thing:
    """Base class for Reddit content"""

    def get_fullname(self):
        return f'{self.prefix}_{self.id}'


class Comment(Thing):
    prefix = 't1'

    def __init__(self):
        pass

class Account(Thing):
    prefix = 't2'

    def __init__(self):
        pass

class Link(Thing):
    prefix = 't3'

    def __init__(self):
        pass

class Message(Thing):
    prefix = 't4'

    def __init__(self):
        pass

class Subreddit(Thing):
    prefix = 't5'

    def __init__(self):
        pass

class Award(Thing):
    prefix = 't3'

    def __init__(self):
        pass

