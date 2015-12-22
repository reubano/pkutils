# pkutils

## Introduction

pkutils is a Python library that simplifies python module packaging.

With pkutils, you can

- Parse requirements files
- Read text files
- and much more...

## Requirements

pkutils has been tested on the following configuration:

- MacOS X 10.9.5
- Python 2.7.9

pkutils requires the following in order to run properly:

- [Python >= 2.7](http://www.python.org/download) (MacOS X comes with python preinstalled)

## Installation

(You are using a [virtualenv](http://www.virtualenv.org/en/latest/index.html), right?)

    sudo pip install pkutils

## Usage

`cat setup.py`

```python
import pkutils

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

requirements = list(pkutils.parse_requirements('requirements.txt'))
dependencies = list(pkutils.parse_requirements('requirements.txt', True))
dev_requirements = list(pkutils.parse_requirements('dev-requirements.txt'))
readme = pkutils.read('README.md')

setup(
    long_description=readme,
    install_requires=requirements,
    tests_require=dev_requirements,
    dependency_links=dependencies,
    classifiers=[
        pkutils.LICENSES['MIT'],
        ...
    ],
    ...
)
```

## Scripts

pkutils comes with a built in task manager `manage.py` and a `Makefile`.

### Setup

    pip install -r dev-requirements.txt

### Examples

*Run python linter and nose tests*

```bash
manage lint
manage test
```

Or if `make` is more your speed...

```bash
make lint
make test
```

## Contributing

View [CONTRIBUTING.rst](https://github.com/reubano/pkutils/blob/master/CONTRIBUTING.rst)

## License

pkutils is distributed under the [MIT License](http://opensource.org/licenses/MIT).
