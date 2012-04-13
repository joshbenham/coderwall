# -*- coding: utf-8 -*-

"""
coderwall.coderwall
~~~~~~~~~~

API for coderwall
"""

import json
import requests

class CoderWall:

  def __init__(self, username):
    response = requests.get('http://coderwall.com/%s.json' % (username))

    if response.status_code != 200:
      raise CoderWall_UserNotFoundError()

    self.user = json.loads(response.text)


class CoderWall_UserNotFoundError(Exception): pass
