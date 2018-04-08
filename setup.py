#!/usr/bin/env python
# -*- coding: utf-8 -*-

import io
import os

from setuptools import setup

# Package meta-data.
NAME = 'etnotify'
DESCRIPTION = 'Notifier script for ETNA.'
URL = 'https://github.com/tbobm/etnotify'
EMAIL = 'massar_t@etna-alternance.net'
AUTHOR = 'Theo "Bob" Massard'
VERSION = 1.3

REQUIRED = [
    'etnawrapper',
]


here = os.path.abspath(os.path.dirname(__file__))

with io.open(os.path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = '\n' + f.read()

# Load the package's __version__.py module as a dictionary.
about = {}
about['__version__'] = VERSION


setup(
    name=NAME,
    version=about['__version__'],
    description=DESCRIPTION,
    long_description=long_description,
    author=AUTHOR,
    author_email=EMAIL,
    url=URL,
    packages=['etnotify'],
    # If your package is a single module, use this instead of 'packages':

    entry_points={
        'console_scripts': ['etnotify=etnotify.etnotify:main'],
    },
    install_requires=REQUIRED,
    include_package_data=True,
    license='MIT',
    classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy'
    ],
)
