#!/usr/bin/env python3
# encoding: utf-8

import requests

from RedditAPI import Reddit
from LogInfo import log_info


r = Reddit(log_info['username'],
           log_info['password'],
           log_info['client_id'],
           log_info['client_secret'],
           log_info['user_agent'])

response = requests.get("https://oauth.reddit.com/api/v1/me", headers=r.headers).json()

print(response)
