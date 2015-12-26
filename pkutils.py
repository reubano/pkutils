# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab

"""
pkutils
~~~~~~~

Provides methods that simplify python module packaging.

Examples:
    parse requirements file::

        requirements = list(parse_requirements('requirements.txt'))

Attributes:
    LICENSES (dict): available python license classifiers.
"""

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

import re
import semver

from os import path as p
from functools import total_ordering
from bisect import bisect
from builtins import *

__version__ = '0.9.0'

__title__ = 'pkutils'
__author__ = 'Reuben Cummings'
__description__ = 'Python packaging utility library'
__email__ = 'reubano@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Reuben Cummings'

LICENSES = {
    'GPL': 'License :: OSI Approved :: GNU General Public License (GPL)',
    'MIT': 'License :: OSI Approved :: MIT License',
    'BSD': 'License :: OSI Approved :: BSD License',
}

STATUSES = [
    'Development Status :: 2 - Pre-Alpha',
    'Development Status :: 3 - Alpha',
    'Development Status :: 4 - Beta',
    'Development Status :: 5 - Production/Stable',
    'Development Status :: 6 - Mature']


@total_ordering
class Version(object):
    """A semver version"""
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return semver.compare(self.value, other.value) == 0

    def __lt__(self, other):
        return semver.compare(self.value, other.value) == -1

    def __str__(self):
        return self.value

    def __repr__(self):
        return '<Version %s>' % self.value


def get_status(version, breaks=None):
    """Categorizes a version into a development status.

    Args:
        version (str): A semver valid version.
        breaks (seq[str]): The version cutoffs

    Returns:
        str: The version status

    Examples:
        >>> get_status('0.3.0') == 'Development Status :: 2 - Pre-Alpha'
        True
        >>> get_status('0.9.0') == 'Development Status :: 3 - Alpha'
        True
    """
    def_breaks = ('0.5.0', '0.10.0', '1.0.0', '2.0.0')
    breakpoints = [Version(b) for b in breaks or def_breaks]
    return STATUSES[bisect(breakpoints, Version(version))]


def read(filename):
    """Reads a file.

    Args:
        filename (str): The file name.

    Returns:
        File content

    Examples:
        >>> read('README.rst').split('\\n')[0] == (
        ...     'pkutils: a Python packaging library')
        True
    """
    try:
        with open(filename, encoding='utf-8') as f:
            return f.read()
    except IOError:
        return ''


def parse_requirements(filename, dep=False):
    """Iteratively parses requirements files. Handles `-r` and `-e` options.

    Args:
        filename (str): The file name.
        dep (bool): Process dependency links (default: False).

    Yields:
        (str): A requirement

    Examples:
        >>> next(parse_requirements('dev-requirements.txt')) == (
        ...     'wheel==0.24.0')
        True
    """
    try:
        with open(filename, encoding='utf-8') as f:
            for line in f:
                candidate = line.strip()

                if candidate.startswith('-r'):
                    parent = p.dirname(filename)
                    new_filename = p.join(parent, candidate[2:].strip())

                    for item in parse_requirements(new_filename, dep):
                        yield item
                elif not dep and '#egg=' in candidate:
                    yield re.sub('.*#egg=(.*)-(.*)', r'\1==\2', candidate)
                elif dep and '#egg=' in candidate:
                    yield candidate.replace('-e ', '')
                elif not dep:
                    yield candidate
    except IOError:
        yield ''
