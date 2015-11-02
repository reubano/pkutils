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

from os import path as p

__version__ = '0.6.1'

__title__ = 'pkutils'
__author__ = 'Reuben Cummings'
__description__ = 'Python Packing utility library'
__email__ = 'reubano@gmail.com'
__license__ = 'MIT'
__copyright__ = 'Copyright 2015 Reuben Cummings'

LICENSES = {
    'GPL': 'License :: OSI Approved :: GNU General Public License (GPL)',
    'MIT': 'License :: OSI Approved :: MIT License',
    'BSD': 'License :: OSI Approved :: BSD License',
}


def read(filename):
    """Reads a file.

    Args:
        filename (str): The file name.

    Returns:
        File content

    Examples:
        >>> read('README.md').split('\\n')[0]
        u'# pkutils'
    """
    try:
        with open(filename) as f:
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
        >>> parse_requirements('dev-requirements.txt').next()
        'wheel==0.22.0'
    """
    with open(filename) as f:
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
