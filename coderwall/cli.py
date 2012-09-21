#! -*- coding: utf-8 -*-

"""
coderwall.cli
~~~~~~~~~~~~~

CLI for coderwall
"""

import sys
from clint import args
from clint.textui import indent, puts
from clint.textui.colored import cyan
from requests.exceptions import ConnectionError

from user import User, User_UserNotFoundError


def main():
    if len(args) != 1:
        puts('Usage' + cyan(': ') + 'coderwall ' + cyan('<') + 'username' + cyan('>'))
        sys.exit(1)

    try:
        coderwall = User(args.get(0))
    except ConnectionError:
        puts('Error' + cyan(': ') + 'There seems to be a problem with the internet')
        sys.exit(1)
    except User_UserNotFoundError:
        puts('Error' + cyan(': ') + '%s does not seem to be a CoderWall user' % (args.get(0)))
        sys.exit(1)

    user = coderwall.user
    puts(user.get('name') + cyan(' (') + user.get('username') + cyan('), ') +
        user.get('location') + cyan(',') + ' Endorsed ' + cyan(str(user.get('endorsements'))) + ' times')

    puts('Badges' + cyan(':'))
    with indent(3):
        for badge in user.get('badges'):
            puts('%s%s%s %s' % (cyan('('), badge['name'], cyan(')'), badge['description']))
