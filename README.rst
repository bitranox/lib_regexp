lib_regexp
==========

|Pypi Status| |license| |maintenance|

|Build Status| |Codecov Status| |Better Code| |code climate| |code climate coverage| |snyk security|

.. |license| image:: https://img.shields.io/github/license/webcomics/pywine.svg
   :target: http://en.wikipedia.org/wiki/MIT_License
.. |maintenance| image:: https://img.shields.io/maintenance/yes/2021.svg
.. |Build Status| image:: https://travis-ci.org/bitranox/lib_regexp.svg?branch=master
   :target: https://travis-ci.org/bitranox/lib_regexp
.. for the pypi status link note the dashes, not the underscore !
.. |Pypi Status| image:: https://badge.fury.io/py/lib-regexp.svg
   :target: https://badge.fury.io/py/lib_regexp
.. |Codecov Status| image:: https://codecov.io/gh/bitranox/lib_regexp/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/bitranox/lib_regexp
.. |Better Code| image:: https://bettercodehub.com/edge/badge/bitranox/lib_regexp?branch=master
   :target: https://bettercodehub.com/results/bitranox/lib_regexp
.. |snyk security| image:: https://snyk.io/test/github/bitranox/lib_regexp/badge.svg
   :target: https://snyk.io/test/github/bitranox/lib_regexp
.. |code climate| image:: https://api.codeclimate.com/v1/badges/d854dda63a0f89c04032/maintainability
   :target: https://codeclimate.com/github/bitranox/lib_regexp/maintainability
   :alt: Maintainability
.. |code climate coverage| image:: https://api.codeclimate.com/v1/badges/d854dda63a0f89c04032/test_coverage
   :target: https://codeclimate.com/github/bitranox/lib_regexp/test_coverage
   :alt: Code Coverage

some convenience functions for regexp

automated tests, Travis Matrix, Documentation, Badges for this Project are managed with `lib_travis_template <https://github
.com/bitranox/lib_travis_template>`_ - check it out

supports python 3.6-3.8, pypy3 and possibly other dialects.

`100% code coverage <https://codecov.io/gh/bitranox/lib_regexp>`_, mypy static type checking, tested under `Linux, macOS, Windows and Wine <https://travis-ci
.org/bitranox/lib_regexp>`_, automatic daily builds  and monitoring

----

- `Installation and Upgrade`_
- `Usage`_
- `Usage from Commandline`_
- `Requirements`_
- `Acknowledgements`_
- `Contribute`_
- `Report Issues <https://github.com/bitranox/lib_regexp/blob/master/ISSUE_TEMPLATE.md>`_
- `Pull Request <https://github.com/bitranox/lib_regexp/blob/master/PULL_REQUEST_TEMPLATE.md>`_
- `Code of Conduct <https://github.com/bitranox/lib_regexp/blob/master/CODE_OF_CONDUCT.md>`_
- `License`_
- `Changelog`_

----

Installation and Upgrade
------------------------

Before You start, its highly recommended to update pip and setup tools:


.. code-block:: bash

    python3 -m pip --upgrade pip
    python3 -m pip --upgrade setuptools
    python3 -m pip --upgrade wheel


install latest version with pip (recommended):

.. code-block:: bash

    # upgrade all dependencies regardless of version number (PREFERRED)
    python3 -m pip install --upgrade git+https://github.com/bitranox/lib_regexp.git --upgrade-strategy eager

    # test without installing (can be skipped)
    python3 -m pip install git+https://github.com/bitranox/lib_regexp.git --install-option test

    # normal install
    python3 -m pip install --upgrade git+https://github.com/bitranox/lib_regexp.git


install latest pypi Release (if there is any):

.. code-block:: bash

    # latest Release from pypi
    python3 -m pip install --upgrade lib_regexp

    # test without installing (can be skipped)
    python3 -m pip install lib_regexp --install-option test

    # normal install
    python3 -m pip install --upgrade lib_regexp



include it into Your requirements.txt:

.. code-block:: bash

    # Insert following line in Your requirements.txt:
    # for the latest Release on pypi (if any):
    lib_regexp
    # for the latest Development Version :
    lib_regexp @ git+https://github.com/bitranox/lib_regexp.git

    # to install and upgrade all modules mentioned in requirements.txt:
    python3 -m pip install --upgrade -r /<path>/requirements.txt


Install from source code:

.. code-block:: bash

    # cd ~
    $ git clone https://github.com/bitranox/lib_regexp.git
    $ cd lib_regexp

    # test without installing (can be skipped)
    python3 setup.py test

    # normal install
    python3 setup.py install


via makefile:

if You are on linux, makefiles are a very convenient way to install. Here we can do much more, like installing virtual environment, clean caches and so on.
This is still in development and not recommended / working at the moment:

.. code-block:: shell

    # from Your shell's homedirectory:
    $ git clone https://github.com/bitranox/lib_regexp.git
    $ cd lib_regexp

    # to run the tests:
    $ make test

    # to install the package
    $ make install

    # to clean the package
    $ make clean

    # uninstall the package
    $ make uninstall

Usage
-----------

.. code-block::

    import the module and check the code - its easy and documented there, including doctest examples.
    in case of any questions the usage section might be expanded at a later time

Usage from Commandline
------------------------

.. code-block:: bash

   Usage:
       lib_regexp (-h | -v | -i)

   Options:
       -h, --help          show help
       -v, --version       show version
       -i, --info          show Info

   this module exposes no other useful functions to the commandline

Requirements
------------
following modules will be automatically installed :

.. code-block:: bash

    ## Project Requirements
    docopt

Acknowledgements
----------------

- special thanks to "uncle bob" Robert C. Martin, especially for his books on "clean code" and "clean architecture"

Contribute
----------

I would love for you to fork and send me pull request for this project.
- `please Contribute <https://github.com/bitranox/lib_regexp/blob/master/CONTRIBUTING.md>`_

License
-------

This software is licensed under the `MIT license <http://en.wikipedia.org/wiki/MIT_License>`_

---

Changelog
=========

0.0.2
-----
development

0.0.1
-----
2019-09-03: Initial public release

