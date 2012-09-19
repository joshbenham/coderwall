# -*- coding: utf-8 -*-

"""
coderwall.coderwall
~~~~~~~~~~

API for coderwall
"""

import json
import requests


class User:

    def __init__(self, username):
        """Query coderwall to fetch the user"""
        response = requests.get('http://coderwall.com/%s.json' % (username))

        if response.status_code != 200:
            raise User_UserNotFoundError()

        self.user = json.loads(response.text)


class User_UserNotFoundError(Exception):
    pass
