Installation
------------

(You are using a `virtualenv`_, right?)

At the command line, install pkutils using either ``pip`` (recommended)

.. code-block:: bash

    pip install pkutils

or ``easy_install``

.. code-block:: bash

    easy_install pkutils

Detailed installation instructions
----------------------------------

If you have `virtualenvwrapper`_ installed, at the command line type:

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

.. _virtualenv: http://www.virtualenv.org/en/latest/index.html
.. _virtualenvwrapper: https://virtualenvwrapper.readthedocs.org/en/latest/
