pkutils: a Python packaging library
===================================

|travis| |versions| |pypi|

Index
-----
`Introduction`_ | `Requirements`_ | `Motivation`_ | `Usage`_ | `Installation`_ |
`Project Structure`_ | `Design Principles`_ | `Scripts`_ | `Contributing`_ | `License`_

Introduction
------------

pkutils is a Python library_ that simplifies python module packaging. It is
intended to be used in your package's ``setup.py`` file.

With pkutils, you can

- Parse requirements files
- Determine your project's development status
- Read text files
- and much more...

Requirements
------------

pkutils has been tested and is known to work on Python 2.7, 3.5, and 3.6;
PyPy2.7; and PyPy3.5.

Motivation
----------

Python has a great packaging system, but to actually create and publish a
package requires a lot of work to do well. I designed pkutils to provide
many useful packaging use-cases out of the box. For example, to automatically
include the contents of your ``requirements.txt`` file, simply add the following
to ``setup.py``:

.. code-block:: python

    import pkutils

    ...

    requirements = list(pkutils.parse_requirements('requirements.txt'))
    dev_requirements = list(pkutils.parse_requirements('dev-requirements.txt'))

    setup(
        ...
        install_requires=requirements,
        tests_require=dev_requirements,
        ...)

.. _library:

Usage
-----

pkutils is intended to be used directly as a Python library.

``my_package/__init__.py``

.. code-block:: python

    __version__ = '0.5.4'

    __title__ = 'my_package'
    __author__ = 'Reuben Cummings'
    __description__ = 'My super awesome great package'
    __email__ = 'reubano@gmail.com'
    __license__ = 'MIT'
    __copyright__ = 'Copyright 2015 Reuben Cummings'

``setup.py``

.. code-block:: python

    import pkutils

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    requirements = list(pkutils.parse_requirements('requirements.txt'))
    dependencies = list(pkutils.parse_requirements('requirements.txt', True))
    dev_requirements = list(pkutils.parse_requirements('dev-requirements.txt'))
    readme = pkutils.read('README.rst')
    module = pkutils.parse_module('my_package/__init__.py')
    version = module.__version__
    project = module.__title__
    user = 'reubano'

    setup(
        name=project,
        version=version,
        description=module.__description__,
        long_description=readme,
        author=module.__author__,
        author_email=module.__email__,
        install_requires=requirements,
        tests_require=dev_requirements,
        dependency_links=dependencies,
        setup_requires=['pkutils'],
        url=pkutils.get_url(project, user),
        download_url=pkutils.get_dl_url(project, user, version),
        classifiers=[
            pkutils.LICENSES['MIT'],
            pkutils.get_status(version),
            ...
        ],
        ...
    )

This is then converted into something like the following:

.. code-block:: python

    ...

    setup(
        name='my_package',
        version='0.5.4',
        description='My super awesome great package',
        long_description='my_package: a super awesome great...',
        author='Reuben Cummings',
        author_email='reubano@gmail.com',
        install_requires=['semver==2.2.1'],
        tests_require=['semver==2.2.1', 'wheel==0.24.0', 'flake8==2.5.1', ...],
        dependency_links=[],
        setup_requires=['pkutils'],
        url='https://github.com/reubano/pkutils',
        download_url='https://github.com/reubano/pkutils/archive/v0.5.4.tar.gz',
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Development Status :: 4 - Beta',
            ...
        ],
        ...
    )

Installation
------------

(You are using a `virtualenv`_, right?) [#]_

At the command line, install pkutils using either ``pip`` (*recommended*)

.. code-block:: bash

    pip install -u pkutils

or ``easy_install``

.. code-block:: bash

    easy_install pkutils

Please see the `installation doc`_ for more details.

Project Structure
-----------------

.. code-block:: bash

    ┌── CHANGES.rst
    ├── CONTRIBUTING.rst
    ├── LICENSE
    ├── MANIFEST.in
    ├── Makefile
    ├── README.md
    ├── dev-requirements.txt
    ├── helpers
    │   ├── check-stage
    │   ├── clean
    │   ├── srcdist
    │   ├── test
    │   └── wheel
    ├── manage.py
    ├── pkutils.py
    ├── requirements.txt
    ├── setup.cfg
    ├── setup.py
    ├── tests
    │   ├── __init__.py
    │   └── standard.rc
    └── tox.ini

Design Principles
-----------------

- minimize external dependencies
- prefer functions over objects
- keep the API as simple as possible

Scripts
-------

pkutils comes with a built in task manager ``manage.py``

Setup
~~~~~

.. code-block:: bash

    pip install -r dev-requirements.txt

Examples
~~~~~~~~

*View available commands*

.. code-block:: bash

    manage

*Show help for a given command*

.. code-block:: bash

    manage <command> -h

*Run python linter and nose tests*

.. code-block:: bash

    manage lint
    manage test

Or if ``make`` is more your speed...

.. code-block:: bash

    make lint
    make test

Contributing
------------

Please mimic the coding style/conventions used in this repo.
If you add new classes or functions, please add the appropriate doc blocks with
examples. Also, make sure the python linter and nose tests pass.

Please see the `contributing doc`_ for more details.

License
-------

pkutils is distributed under the `MIT License`_.

.. |travis| image:: https://img.shields.io/travis/reubano/pkutils.svg
    :target: https://travis-ci.org/reubano/pkutils

.. |versions| image:: https://img.shields.io/pypi/pyversions/pkutils.svg
    :target: https://pypi.python.org/pypi/pkutils

.. |pypi| image:: https://img.shields.io/pypi/v/pkutils.svg
    :target: https://pypi.python.org/pypi/pkutils

.. _MIT License: http://opensource.org/licenses/MIT
.. _virtualenv: http://www.virtualenv.org/en/latest/index.html
.. _contributing doc: https://github.com/reubano/pkutils/blob/master/CONTRIBUTING.rst
.. _installation doc: https://github.com/reubano/bump/blob/master/INSTALLATION.rst
