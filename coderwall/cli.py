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

def main():
  if len(args) != 1:
    puts(_e('Usage: cw <username>'))
    sys.exit(1)

  try:
    coderwall = CoderWall(args.get(0))
  except CoderWall_UserNotFoundError:
    puts(_e('%s does not seem to be a CoderWall user' % (args.get(0))))
    sys.exit(1)

  user = coderwall.user
  puts(user.get('name') + _s(' (') + user.get('username') + _s('), ') + user.get('location') + _s(',') + ' Endorsed ' + _s(str(user.get('endorsements'))) + ' times')
  
  puts('Badges' + _s(':'))
  with indent(3):
    for badge in user.get('badges'):
      puts('%s%s%s %s' % (_s('('), _p(badge['name']), _s(')'), badge['description']))

# Color: Primary
def _p(s):
  return colored.clean(s)

# Color: Secondary
def _s(s):
  return colored.cyan(s)

# Color: Error
def _e(s):
  return colored.red(s)
