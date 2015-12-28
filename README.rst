pkutils: a Python packaging library
===================================

|travis| |versions| |pypi|

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

pkutils has been tested and is known to work on the following `Python versions`_:

- 2.7
- 3.4
- 3.5
- pypy v4.0
- pypy3 v2.4

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

``setup.py``

.. code-block:: python

    import pkutils
    import my_module

    try:
        from setuptools import setup
    except ImportError:
        from distutils.core import setup

    requirements = list(pkutils.parse_requirements('requirements.txt'))
    dependencies = list(pkutils.parse_requirements('requirements.txt', True))
    dev_requirements = list(pkutils.parse_requirements('dev-requirements.txt'))
    readme = pkutils.read('README.rst')
    version = my_module.__version__
    project = my_module.__title__
    user = 'reubano'

    setup(
        long_description=readme,
        install_requires=requirements,
        tests_require=dev_requirements,
        dependency_links=dependencies,
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
        long_description='pkutils: a Python packaging library...',
        install_requires=['semver==2.2.1'],
        tests_require=['semver==2.2.1', 'wheel==0.24.0', 'flake8==2.5.1', ...],
        dependency_links=[],
        url='https://github.com/reubano/pkutils',
        download_url='https://github.com/reubano/pkutils/archive/v0.11.0.tar.gz',
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

    pip install pkutils

or ``easy_install``

.. code-block:: bash

    easy_install pkutils

Project structure
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

License
-------

pkutils is distributed under the `MIT License`_.

Contributing
------------

Please mimic the coding style/conventions used in this repo.
If you add new classes or functions, please add the appropriate doc blocks with
examples. Also, make sure the python linter and nose tests pass.

Please see the `contributing doc`_ for more details.

.. |travis| image:: https://img.shields.io/travis/reubano/pkutils.svg
    :target: https://travis-ci.org/reubano/pkutils

.. |versions| image:: https://img.shields.io/pypi/pyversions/pkutils.svg
    :target: https://pypi.python.org/pypi/pkutils

.. |pypi| image:: https://img.shields.io/pypi/v/pkutils.svg
    :target: https://pypi.python.org/pypi/pkutils

.. _MIT License: http://opensource.org/licenses/MIT
.. _virtualenv: http://www.virtualenv.org/en/latest/index.html
.. _Python versions: http://www.python.org/download
.. _contributing doc: https://github.com/reubano/pkutils/blob/master/CONTRIBUTING.rst

Footnotes
---------

.. [#] Detailed installation instructions

If you have ``virtualenvwrapper`` installed, at the command line type:

.. code-block:: bash

    mkvirtualenv pkutils
    pip install pkutils

Or, if you only have ``virtualenv`` installed:

.. code-block:: bash

    virtualenv ~/.venvs/pkutils
    source ~/.venvs/pkutils/bin/activate
    pip install pkutils

Otherwise, you can install globally::

    pip install pkutils
