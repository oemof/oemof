#!/usr/bin/env python
# -*- encoding: utf-8 -*-
from __future__ import absolute_import
from __future__ import print_function

import io
import re
from glob import glob
from os.path import basename
from os.path import dirname
from os.path import join
from os.path import splitext

from setuptools import find_packages
from setuptools import setup


def read(*names, **kwargs):
    with io.open(
        join(dirname(__file__), *names),
        encoding=kwargs.get("encoding", "utf8"),
    ) as fh:
        return fh.read()


githuburl = "@https://github.com/oemof/"

setup(
    name="oemof",
    version="1.0",
    license="MIT",
    description=(
        "Open Energy Modelling Framework - Python toolbox for energy"
        " system modelling and optimisation."
    ),
    long_description="%s\n%s"
    % (
        re.compile("^.. start-badges.*^.. end-badges", re.M | re.S).sub(
            "", read("README.rst")
        ),
        re.sub(":[a-z]+:`~?(.*?)`", r"``\1``", read("CHANGELOG.rst")),
    ),
    long_description_content_type="text/x-rst",
    author="oemof developer group",
    author_email="contact@oemof.org",
    url="https://github.com/oemof/oemof",
    packages=find_packages("src"),
    package_dir={"": "src"},
    py_modules=[splitext(basename(path))[0] for path in glob("src/*.py")],
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        # complete classifier list:
        # http://pypi.python.org/pypi?%3Aaction=list_classifiers
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: Unix",
        "Operating System :: POSIX",
        "Operating System :: Microsoft :: Windows",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Utilities",
    ],
    project_urls={
        "Documentation": "https://oemof.readthedocs.io/",
        "Changelog": "https://oemof.readthedocs.io/en/latest/changelog.html",
        "Issue Tracker": "https://github.com/oemof/oemof/issues",
    },
    keywords=[
        # eg: 'keyword1', 'keyword2', 'keyword3',
    ],
    python_requires=">=3.7",
    install_requires=[
        "jinja2",
        "cydets",
        "demandlib",
        "dhnx",
        "feedinlib",
        "oemof.network",
        "oemof.solph",
        "oemof.tools",
        "tespy",
        "windpowerlib",
    ],
)
