#! -*- coding: utf-8 -*-

"""
coderwall.cli
~~~~~~~~~~~~~

CLI for coderwall
"""

import sys
from clint import args
from clint.textui import colored, indent, puts
from coderwall.coderwall import CoderWall, CoderWall_UserNotFoundError
from requests.exceptions import ConnectionError

def main():
  if len(args) != 1:
    puts(_p('Usage') + _s(': ') + _p('coderwall ') + _s('<') + _p('username') + _s('>'))
    sys.exit(1)

  try:
    coderwall = CoderWall(args.get(0))
  except ConnectionError:
    puts(_p('Error') + _s(': ') + _p('There seems to be a problem with the internet'))
    sys.exit(1)
  except CoderWall_UserNotFoundError:
    puts(_p('Error') + _s(': ') + _p('%s does not seem to be a CoderWall user' % (args.get(0))))
    sys.exit(1)

  user = coderwall.user
  puts(_p(user.get('name')) + _s(' (') + _p(user.get('username')) + _s('), ') + _p(user.get('location')) + _s(',') + _p(' Endorsed ') + _s(str(user.get('endorsements'))) + _p(' times'))
  
  puts(_p('Badges') + _s(':'))
  with indent(3):
    for badge in user.get('badges'):
      puts('%s%s%s %s' % (_s('('), _p(badge['name']), _s(')'), _p(badge['description'])))

# Color: Primary
def _p(s):
  return colored.clean(s)

# Color: Secondary
def _s(s):
  return colored.cyan(s)
