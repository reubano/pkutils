# -*- coding: utf-8 -*-
# vim: sw=4:ts=4:expandtab

"""
pkutils
~~~~~~~

Provides methods that simplify python module packaging.

Examples:
    parse requirements file::

        >>> requirements = parse_requirements('requirements.txt')
        >>> len(list(requirements)) > 0
        True
        >>> get_status('0.3.0') == 'Development Status :: 2 - Pre-Alpha'
        True



Attributes:
    LICENSES (dict): available python license classifiers.
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals)

import re

from io import open
from bisect import bisect
from os import path as p
from functools import total_ordering

import semver

__version__ = '0.13.6'

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


class Dictlike(object):
    """Creates an object whose attributes are accessible in a dict like manner.
    """
    def __init__(self, data):
        """ Dictlike constructor

        Args:
            data (dict): The attributes to set

        Examples:
            >>> data = {'one': 1, 'two': 2}
            >>> kw = Dictlike(data)
            >>> kw.one
            1
            >>> kw.two
            2
            >>> kw.get('one')
            1
            >>> kw['two']
            2
            >>> kw.three == kw.get('three') == None
            True
        """
        self.data = data
        self.get = self.data.get

    def __getitem__(self, name):
        return self.data[name]

    def __getattr__(self, name):
        return self.get(name)


@total_ordering
class Version(object):
    """A semver version

    Args:
        version (str): A semver valid version.

    Examples:
        >>> v1 = Version('0.3.0')
        >>> v2 = Version('0.10.0')
        >>> v1, v2
        (<Version 0.3.0>, <Version 0.10.0>)
        >>> str(v1), str(v2)
        ('0.3.0', '0.10.0')
        >>> str(v2) > str(v1)
        False
        >>> v2 > v1
        True
    """
    def __init__(self, value):
        self.value = value

    def __eq__(self, other):
        return semver.compare(self.value, other.value) == 0

    def __lt__(self, other):
        return semver.compare(self.value, other.value) == -1

    def __str__(self):
        return self.value

    def __hash__(self, other):
        return hash(self.value)

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


def get_url(project, user, base='https://github.com'):
    """Gets the repo download url.

    Args:
        user (str): The username.
        base (str): The hosting site (default: 'https://github.com').

    Returns:
        str: The url

    Examples:
        >>> get_url('pkutils', 'reubano') == (
        ...     'https://github.com/reubano/pkutils')
        True
    """
    return '%s/%s/%s' % (base, user, project)


def get_dl_url(project, user, version, base='https://github.com', ext='tar.gz'):
    """Gets the package download url.

    Args:
        version (str): A semver valid version.
        user (str): The username.
        base (str): The hosting site (default: 'https://github.com').
        ext (str): The file extension (default: 'tar.gz').

    Returns:
        str: The download url

    Examples:
        >>> get_dl_url('pkutils', 'reubano', '0.3.0') == (
        ...     'https://github.com/reubano/pkutils/archive/v0.3.0.tar.gz')
        True
    """
    return '%s/%s/%s/archive/v%s.%s' % (base, user, project, version, ext)


def read(filename, encoding='utf-8'):
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
    with open(filename, encoding=encoding) as f:
        return f.read()


def _get_attrs(f):
    """Parses text to extract any double underscored variables.

    Args:
        f (obj): A file like object or iterable of lines of text.

    Yields:
        [Tuple(str, str)]: A tuple of (variable, value).

    Examples:
        >>> lines = ["__version__ = '0.12.4'\\n"]
        >>> next(_get_attrs(lines)) == ('__version__', '0.12.4')
        True
    """
    for line in f:
        if line.startswith('__'):
            splits = line.split('=')
            yield tuple(s.strip().strip("'").strip('"') for s in splits)


def parse_module(filename, encoding='utf-8'):
    """Parses a module file and exposes any double underscored variables as
    object attributes.

    Args:
        filename (str): The file name.

    Returns:
        (obj): An object whose attributes are accessible in a dict like manner.

    Examples:
        >>> from tempfile import NamedTemporaryFile
        >>>
        >>> text = (
        ...     "from os import path as p\\n__version__ = '0.12.4'\\n"
        ...     "__title__ = 'pkutils'\\n__author__ = 'Reuben Cummings'\\n"
        ...     "__email__ = 'reubano@gmail.com'\\n__license__ = 'MIT'\\n")
        >>>
        >>> with NamedTemporaryFile() as f:
        ...     bool(f.write(text.encode('utf-8')) or True)
        ...     bool(f.seek(0) or True)
        ...     module = parse_module(f.name)
        ...     module.__version__ == '0.12.4'
        ...     module.__title__ == module.get('__title__') == 'pkutils'
        ...     module.__email__ == module['__email__'] == 'reubano@gmail.com'
        ...     module.missing == module.get('missing') == None
        True
        True
        True
        True
        True
        True
    """
    with open(filename, encoding=encoding) as f:
        attrs = dict(_get_attrs(f))

    return Dictlike(attrs)


def parse_requirements(filename, dep=False, encoding='utf-8'):
    """Iteratively parses requirements files. Handles `-r` and `-e` options.

    Args:
        filename (str): The file name.
        dep (bool): Process dependency links (default: False).

    Yields:
        (str): A requirement

    Examples:
        >>> next(parse_requirements('dev-requirements.txt')) == (
        ...     'flake8>=2.5.1,<3.0.0')
        True
    """
    with open(filename, encoding=encoding) as f:
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
