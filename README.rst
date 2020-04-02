========
Overview
========

.. start-badges

.. list-table::
    :stub-columns: 1

    * - docs
      - |docs|
    * - tests
      - | |travis| |appveyor| |requires|
        | |codecov|
    * - package
      - | |version| |wheel| |supported-versions| |supported-implementations|
        | |commits-since|
.. |docs| image:: https://readthedocs.org/projects/oemof/badge/?style=flat
    :target: https://readthedocs.org/projects/oemof
    :alt: Documentation Status

.. |travis| image:: https://api.travis-ci.org/oemof/oemof.svg?branch=master
    :alt: Travis-CI Build Status
    :target: https://travis-ci.org/oemof/oemof

.. |appveyor| image:: https://ci.appveyor.com/api/projects/status/github/oemof/oemof?branch=master&svg=true
    :alt: AppVeyor Build Status
    :target: https://ci.appveyor.com/project/oemof/oemof

.. |requires| image:: https://requires.io/github/oemof/oemof/requirements.svg?branch=master
    :alt: Requirements Status
    :target: https://requires.io/github/oemof/oemof/requirements/?branch=master

.. |codecov| image:: https://codecov.io/gh/oemof/oemof/branch/master/graphs/badge.svg?branch=master
    :alt: Coverage Status
    :target: https://codecov.io/github/oemof/oemof

.. |version| image:: https://img.shields.io/pypi/v/oemof.svg
    :alt: PyPI Package latest release
    :target: https://pypi.org/project/oemof

.. |wheel| image:: https://img.shields.io/pypi/wheel/oemof.svg
    :alt: PyPI Wheel
    :target: https://pypi.org/project/oemof

.. |supported-versions| image:: https://img.shields.io/pypi/pyversions/oemof.svg
    :alt: Supported versions
    :target: https://pypi.org/project/oemof

.. |supported-implementations| image:: https://img.shields.io/pypi/implementation/oemof.svg
    :alt: Supported implementations
    :target: https://pypi.org/project/oemof

.. |commits-since| image:: https://img.shields.io/github/commits-since/oemof/oemof/v0.4.0.beta0.svg
    :alt: Commits since latest release
    :target: https://github.com/oemof/oemof/compare/v0.4.0.beta0...master



.. end-badges

Open Energy Modelling Framework - Python toolbox for energy system modelling and optimisation.

The omeof project aims to be a loose organisational frame for tools in the wide field of (energy) system modelling. 
Every project is managed by their own developer team but we share some developer and design rules to make it easier to understand each others tools.

All projects are in different states and some even may not have a stable release but all projects are open to join.
We do not belong to a specific institution and everybody is free to join the developer teams and will have the same rights.
There is no higher decission level.

This repository is also used to organise everything for the oemof community. 

- Webconference dates
- Real life meetings
- Website and Mailinglist
- General communication

Projects with stable releases
=============================

* `oemof-solph <https://github.com/oemof/oemof-solph>`_
* `TESPy <https://github.com/oemof/tespy>`_


Projects in an early state
==========================

* ...


All project libraries are free software licenced under the MIT license.



Installation
============

::

    pip install oemof

You can also install the in-development version with::

    pip install https://github.com/oemof/oemof/archive/master.zip


Documentation
=============


https://oemof.readthedocs.io/


Development
===========

To run the all tests run::

    tox

Note, to combine the coverage data from all the tox environments run:

.. list-table::
    :widths: 10 90
    :stub-columns: 1

    - - Windows
      - ::

            set PYTEST_ADDOPTS=--cov-append
            tox

    - - Other
      - ::

            PYTEST_ADDOPTS=--cov-append tox
