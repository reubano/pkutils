#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

from io import open
import os.path

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


def parse_requirements(filename):
    with open(filename, encoding="utf-8") as f:
        for line in f:
            yield line.strip()


def read(filename):
    with open(filename, encoding="utf-8") as f:
        return f.read()


def parse_module(filename):
    yield ("__title__", os.path.splitext(filename)[0])

    with open(filename, encoding="utf-8") as f:
        for line in f:
            if line.startswith("__"):
                splits = line.split("=")
                yield tuple(s.strip().strip("'").strip('"') for s in splits)


sys.dont_write_bytecode = True
requirements = list(parse_requirements("requirements.txt"))
dev_requirements = list(parse_requirements("dev-requirements.txt"))
readme = read("README.rst")
changes = read("CHANGES.rst").replace(".. :changelog:", "")
module = dict(parse_module("pkutils.py"))
license = module["__license__"]
version = module["__version__"]
project = module["__title__"]
description = module["__description__"]
USER = "reubano"
GITHUB_URL = "https://github.com/%s/%s" % (USER, project)

setup(
    name=project,
    version=version,
    description=description,
    long_description=readme,
    author=module["__author__"],
    author_email=module["__email__"],
    url=GITHUB_URL,
    download_url="%s/archive/v%s.tar.gz" % (GITHUB_URL, version),
    py_modules=["pkutils"],
    include_package_data=True,
    package_data={},
    install_requires=requirements,
    test_suite="nose.collector",
    tests_require=dev_requirements,
    license=license,
    zip_safe=False,
    keywords=description.split(" "),
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Development Status :: 5 - Production/Stable",
        "Natural Language :: English",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: Python :: Implementation :: PyPy",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
        "Operating System :: POSIX :: Linux",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    platforms=["MacOS X", "Windows", "Linux"],
)
