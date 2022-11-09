=======================================
Open Energy Modelling Framework (oemof)
=======================================
.. start-badges

.. comment
    .. list-table::
        :stub-columns: 1


|docs|

.. |docs| image:: https://readthedocs.org/projects/oemof/badge/?style=flat
        :target: https://readthedocs.org/projects/oemof
        :alt: Documentation Status

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


Installation
============

The oemof package is a meta package an will install all (!) oemof packages. This
is usually not what you want to do. Use the list above to install the packages
you need.


Documentation
=============


The meta `documentation of oemof <https://oemof.readthedocs.io>`_ is hosted on ReadTheDocs.


Development
===========

To run all tests run::

    tox
