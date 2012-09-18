# -*- coding: utf-8 -*-
#
#  setup.py
#  coderwall
#
#  Created by Josh Benham.

"""
The package configuration for coderwall.
"""

from setuptools import setup

with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

with open('requirements.txt') as f:
    requirements = f.read()

setup(
    name='coderwall',
    version='0.0.1',
    description='CoderWall command line interface to retrieve users statistics',
    long_description=readme,
    keywords='web python coderwall statistics cli terminal',
    author='Josh Benham',
    author_email='joshbenham@gmail.com',
    url='https://github.com/joshbenham/coderwall',
    license=license,
    classifiers=[
        "Programming Language :: Python",
    ],
    packages=['coderwall'],
    scripts=['coderwall_r'],
    install_requires=requirements,
)
