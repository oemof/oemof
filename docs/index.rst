Open Energy Modelling Framework (oemof)
=======================================

The open energy modelling framework (oemof) refers to a collection of python libraries for energy symtem modelling that are open source licensed.
Originally, it was developed a as single library to ease the process of creating energy system models for the heat and power sector.
Today, it is distinguished into several :ref:`packages_label` that each is specified for a certain task in the energy system modeling process.
Sometimes, due to historical reasons, oemof gets mixed up with the most recognised oemof library `oemof-solph <https://oemof-solph.readthedocs.io>`_ which is used for building LP/MILP energy system models.

In 2014, the oemof developing group was founded by researchers from the Center for Sustainable Energy Systems (ZNES) Flensburg together with the Reiner Lemoine Institute (RLI) in Berlin.
Later, researchers from other research institutions joined this loosly-organised group of people that maintain the oemof libraries.
The main motivation for the initiative was to provide tools for recurring tasks in energy system modelling.
Because oemof was developed in an academic context, scientific standards (transparency, repeatability, reproducibility, and scrutiny) were important.
Energy system models often do not have publicly accessible source code, missing freely available data, and are poorly documented. This creates barriers for scientific progress in energy system modelling and analysis.
In addition, energy system model code often cannot be re-used because of legal and practical issues.
The development of oemof addresses these problems by offering a free, open and clearly documented framework for energy system modelling.
The open source approach allows a collaborative development of the framework that offers several advantages:

- **Synergies** - By developing collaboratively synergies between the participating institutes can be utilized.
- **Debugging** - Through the input of a larger group of users and developers bugs are identified and fixed at an earlier stage.
- **Advancement** - The oemof-based application profits from further development of the framework.

To get an idea what's possible to do with the oemof libraries, take a look on `models <https://oemof.org/models/>`_ that are built based on oemof libraries, `publications <https://oemof.org/publications/>`_ that use oemof tools for generating underlying results, and `projects <https://oemof.org/projects/>`_ that are related to the development or simly use oemof tools as building blocks.
Furthermore, visit the documentation of the individual oemof :ref:`packages_label`.

`This repository <https://github.com/oemof/oemof>`_ contains no code and is only used for organising the oemof community, for example

- User and developer meetings
- Webconference dates
- New packages
- Website and Mailinglist
- General communication

You can find recent topics of discussion in the `issues <https://github.com/oemof/oemof/issues>`_.

We're are happy about any kind of contribution. Read more about it in :ref:`contributing_label`.


Read more
---------

.. toctree::
   :maxdepth: 2

   packages
   contributing


