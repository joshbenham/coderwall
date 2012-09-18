#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from clint.textui import colored


def p(s):
    """Color: Primary"""
    return colored.clean(s)


def s(s):
    """Color: Secondary"""
    return colored.cyan(s)
