#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pkutils

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

sys.dont_write_bytecode = True
dev_requirements = list(pkutils.parse_requirements('dev-requirements.txt'))
readme = pkutils.read('README.md')
changes = pkutils.read('CHANGES.rst').replace('.. :changelog:', '')
license = pkutils.__license__

setup(
    name=pkutils.__title__,
    version=pkutils.__version__,
    description=pkutils.__description__,
    long_description=readme,
    author=pkutils.__author__,
    author_email=pkutils.__email__,
    url='https://github.com/reubano/pkutils',
    py_modules=['pkutils'],
    include_package_data=True,
    install_requires=[],
    tests_require=dev_requirements,
    license=license,
    zip_safe=False,
    keywords=pkutils.__title__,
    classifiers=[
        'Development Status :: 4 - Beta',
        'License :: OSI Approved :: %s' % pkutils.LICENSES[license],
        'Natural Language :: English',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Intended Audience :: End Users/Desktop',
        'Operating System :: MacOS :: MacOS X',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
    ],
    platforms=['MacOS X', 'Windows', 'Linux'],
)
