pkutils: a Python packaging library
===================================

|versions| |pypi|

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

- 2.7.10

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

Complete Example
~~~~~~~~~~~~~~~~

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

    setup(
        long_description=readme,
        install_requires=requirements,
        tests_require=dev_requirements,
        dependency_links=dependencies,
        classifiers=[
            pkutils.LICENSES['MIT'],
            pkutils.get_status(my_module.__version__),
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
        classifiers=[
            'License :: OSI Approved :: MIT License',
            'Development Status :: 3 - Alpha',
            ...
        ],
        ...
    )

Installation
------------

(You are using a `virtualenv`_, right?) [#]_

At the command line, install pygogo using either ``pip`` (*recommended*)

.. code-block:: bash

    pip install pypygogo

or ``easy_install``

.. code-block:: bash

    easy_install pygogo

.. [#] Detailed installation instructions

If you have ``virtualenvwrapper`` installed, at the command line type:

.. code-block:: bash

    mkvirtualenv pygogo
    pip install pygogo

Or, if you only have ``virtualenv`` installed:

.. code-block:: bash

    virtualenv ~/.venvs/pygogo
    source ~/.venvs/pygogo/bin/activate
    pip install pygogo

Otherwise, you can install globally::

    pip install pygogo

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

.. |versions| image:: https://img.shields.io/pypi/pyversions/pkutils.svg
    :target: https://pypi.python.org/pypi/pkutils

.. |pypi| image:: https://img.shields.io/pypi/v/pkutils.svg
    :target: https://pypi.python.org/pypi/pkutils

.. _MIT License: http://opensource.org/licenses/MIT
.. _virtualenv: http://www.virtualenv.org/en/latest/index.html
.. _Python versions: http://www.python.org/download
.. _contributing doc: https://github.com/reubano/pkutils/blob/master/CONTRIBUTING.rst
