.. _using_oemof_label:

=====
Usage
=====

Open Energy Modelling Framework - Python toolbox for energy system modelling and optimisation.

The omeof project aims to be a loose organisational frame for tools in the wide field of (energy) system modelling.

.. contents:: `Current oemof libraries`
    :depth: 1
    :local:
    :backlinks: top


`oemof-solph <https://github.com/oemof/oemof-solph>`_
=====================================================
The `solph <https://github.com/oemof/oemof-solph>`_ library is designed to create and solve linear or mixed-integer linear optimization problems. It is based on optimization modelling language pyomo.

To use solph at least one linear solver has to be installed on your system. Solph is tested with the open source solver `cbc` and the `gurobi` solver (free for academic use). The open `glpk` solver recently showed some odd behaviour, but it should work for small systems.

The formulation of the energy system is based on the oemof-network library but contains additional components such as storages. Furthermore the network class are enhanced with additional parameters such as efficiencies, bounds, cost and more. See the API documentation for more details. Try the `examples <https://github.com/oemof/oemof_examples>`_ to learn how to build a linear energy system.


`oemof-thermal <https://github.com/oemof/oemof-thermal>`_
=========================================================

`oemof.thermal <https://github.com/oemof/oemof-thermal>`_ is an oemof library with a focus on thermal energy technologies (heating/cooling). In its original intention it is an extension to the components of the optimization framework oemof.solph. However, some of its functions may be useful for their own.


`cydets <https://github.com/oemof/cydets>`_
=================================================

Cycle Detection in Time Series (CyDeTS). An algorithm to detect cycles in times series along with their respective depth-of-cycle (DoC) and duration.



`demandlib <https://github.com/oemof/demandlib>`_
=================================================

The `demandlib <https://github.com/oemof/demandlib>`_ library can be used to create load profiles for elctricity and heat knowing the annual demand. See the `documentation of the demandlib <https://demandlib.readthedocs.io/en/latest/>`_ for examples and a full description of the library.


`feedinlib <https://github.com/oemof/feedinlib>`_
=================================================

The `feedinlib <https://github.com/oemof/feedinlib>`_ library serves as an interface between Open Data weather data and libraries to calculate feedin timeseries for fluctuating renewable energy sources.

It is currently under revision (see `here <https://github.com/oemof/feedinlib/issues/29>`_ for further information). To begin with it will provide an interface to the `pvlib <https://github.com/pvlib/pvlib-python>`_ and `windpowerlib <https://github.com/wind-python/windpowerlib>`_ and functions to download MERRA2 weather data and `open_FRED weather data <https://openfredproject.wordpress.com>`_.
See `documentation of the feedinlib <https://feedinlib.readthedocs.io/en/stable/>`_ for a full description of the library.


`tespy <https://github.com/oemof/tespy>`_
=========================================

Thermal Engineering Systems in Python
(`TESPy <https://github.com/oemof/tespy>`_) allows you to calculate
stationary operation in order to design the process of thermal energy systems.
From that point it is possible to simulate the offdesign behavior of your
plant using underlying characteristics for each of the plants components.
The package inlcudes basic components, such as turbines, pumps, compressors,
heat exchangers, pipes, mixers and splitters as well as some advanced
components (e. g. including combustion, derivatives of heat exchangers, drum).

