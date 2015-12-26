#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import (
    absolute_import, division, print_function, with_statement,
    unicode_literals)

import sys
import pkutils

from builtins import *

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.dont_write_bytecode = True
requirements = list(pkutils.parse_requirements('requirements.txt'))
dev_requirements = list(pkutils.parse_requirements('dev-requirements.txt'))
readme = pkutils.read('README.rst')
changes = pkutils.read('CHANGES.rst').replace('.. :changelog:', '')
license = pkutils.__license__
version = pkutils.__version__
title = pkutils.__title__
description = pkutils.__description__
gh = 'https://github.com/reubano'

if sys.version_info.major == 2:
    requirements.append('future==0.15.2')

setup(
    name=title,
    version=version,
    description=description,
    long_description=readme,
    author=pkutils.__author__,
    author_email=pkutils.__email__,
    url='%s/%s' % (gh, title),
    download_url='%s/%s/downloads/%s*.tgz' % (gh, title, title),
    py_modules=['pkutils'],
    include_package_data=True,
    package_data={},
    install_requires=requirements,
    test_suite='nose.collector',
    tests_require=dev_requirements,
    license=license,
    zip_safe=False,
    keywords=[title] + description.split(' '),
    classifiers=[
        pkutils.LICENSES[license],
        'Development Status :: 4 - Beta',
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Intended Audience :: Developers',
        'Operating System :: POSIX :: Linux',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: Microsoft :: Windows',
    ],
    platforms=['MacOS X', 'Windows', 'Linux'],
)
