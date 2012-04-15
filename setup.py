from setuptools import setup

setup(name='coderwall',
  version='0.1',
  description='CoderWall command line interface to retrieve users statistics',
  long_description=open('README.md').read(),
  classifiers=[
    "Programming Language :: Python",
  ],
  author="Josh Benham",
  author_email='joshbenham@gmail.com',
  url='https://github.com/joshbenham/coderwall',
  keywords='web python coderwall statistics cli terminal',
  packages=['coderwall',],
  scripts=['coderwall_r'],
  install_requires=open('requirements.txt').read(),
)

