=======================================
Open Energy Modelling Framework (oemof)
=======================================
.. start-badges

.. comment
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

    .. |appveyor| image:: https://ci.appveyor.com/api/projects/status/0ri9bxniy0irw4j0/branch/master?svg=true
        :alt: AppVeyor Build Status
        :target: https://ci.appveyor.com/project/oemof-developer/oemof

    .. |requires| image:: https://requires.io/github/oemof/oemof/requirements.svg?branch=master
        :alt: Requirements Status
        :target: uvchikuvchik

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

|docs| |travis|

.. |docs| image:: https://readthedocs.org/projects/oemof/badge/?style=flat
        :target: https://readthedocs.org/projects/oemof
        :alt: Documentation Status
.. |travis| image:: https://api.travis-ci.org/oemof/oemof.svg?branch=master
        :alt: Travis-CI Build Status
        :target: https://travis-ci.org/oemof/oemof

.. end-badges

.. figure:: logo/logo_oemof_big.svg

The Open Energy Modelling Framework (oemof) is a Python toolbox for energy system modelling and optimisation.

The oemof project aims to be a loose organisational frame for tools in the wide field of (energy) system modelling.
Every project is managed by their own developer team but we share some developer and design rules to make it easier to understand each other's tools. All project libraries are free software licenced under the MIT license.

All projects are in different stages of implementation, some even may not have a stable release, but all projects are open to be joined by interested people.
We do not belong to a specific institution and everybody is free to join the developer teams and will have the same rights.
There is no higher decision level.


`This repository <https://github.com/oemof/oemof>`_ is also used to organise everything for the oemof community.

- Webconference dates
- Real life meetings
- Website and Mailinglist
- General communication

You can find recent topics of discussion in the `issues <https://github.com/oemof/oemof/issues>`_.

**Overview**

.. contents::
    :depth: 3
    :local:
    :backlinks: top

Projects with stable releases
=============================

* `oemof-solph <https://github.com/oemof/oemof-solph>`_
   A model generator for energy system modelling and optimisation (LP/MILP) -
   (formerly know as `oemof`).

   .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.596235.svg
      :target: https://doi.org/10.5281/zenodo.596235

* `oemof-thermal <https://github.com/oemof/oemof-thermal>`_
   .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3606384.svg
      :target: https://doi.org/10.5281/zenodo.3606384

* `cydets <https://github.com/oemof/cydets>`_
   Cycle Detection in Time Series (CyDeTS). An algorithm to detect cycles in times series along with their respective depth-of-cycle (DoC) and duration.

   .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.2625698.svg
      :target: https://doi.org/10.5281/zenodo.2625698

* `demandlib <https://github.com/oemof/demandlib>`_
   The `demandlib <https://github.com/oemof/demandlib>`_ library can be used to create load profiles for elctricity and heat knowing the annual demand. See the `documentation of the demandlib <http://demandlib.readthedocs.io/en/latest/>`_ for examples and a full description of the library.

   .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.2553504.svg
      :target: https://doi.org/10.5281/zenodo.2553504

* `feedinlib <https://github.com/oemof/feedinlib>`_
   The `feedinlib <https://github.com/oemof/feedinlib>`_ library serves as an interface between Open Data weather data and libraries to calculate feedin timeseries for fluctuating renewable energy sources.

   .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.2554101.svg
      :target: https://doi.org/10.5281/zenodo.2554101

* `TESPy <https://github.com/oemof/tespy>`_
   Thermal Engineering Systems in Python (TESPy). This package provides a powerful simulation toolkit for thermal engineering plants such as power plants, district heating systems or heat pumps.

   .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.2555866.svg
      :target: https://doi.org/10.5281/zenodo.2555866

* `windpowerlib <https://github.com/wind-python/windpowerlib>`_
   The windpowerlib is a library that provides a set of functions and classes
   to calculate the power output of wind turbines. It was originally part of
   the feedinlib (windpower and photovoltaic) but was taken out to build up
   a community concentrating on wind power models.

   .. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.824267.svg
      :target: https://doi.org/10.5281/zenodo.824267


Projects in an early state
==========================

* `DHNx <https://github.com/oemof/dhnx>`_
   District heating system optimisation and simulation models

* `hydropowerlib <https://github.com/hydro-python/hydropowerlib>`_
   The hydropowerlib is designed to calculate feedin time series of run-of-the-river hydropower plants.


Installation
============

It is not possible to install the meta package `oemof`. Use the installation
guide of the package you want to install from the list above.

Be aware that there are still some packages called `oemof` on pypi. These are
old versions of `oemof.solph`. See the `oemof-solph <https://github.com/oemof/oemof-solph>`_ repository for the actual version.


Documentation
=============


The meta `documentation of oemof <https://oemof.readthedocs.io>`_ is hosted on ReadTheDocs.


Development
===========

To run all tests run::

    tox
