#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the
#     PyLABF Project (https://github.com/juniors90/PyLABF/).
# Copyright (c) 2022, Ferreira Juan David
# License: MIT
# Full Text: 
#    https://github.com/juniors90/PyLABF/blob/master/LICENSE

# =============================================================================
# DOCS
# =============================================================================

"""This file is for distribute and install PyLABF"""

# =============================================================================
# IMPORTS
# =============================================================================

import os
import pathlib

from setuptools import setup  # noqa

# =============================================================================
# CONSTANTS
# =============================================================================

PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))


REQUIREMENTS = [
]

with open(PATH / "pylabf" / "__init__.py") as fp:
    for line in fp.readlines():
        if line.startswith("__version__ = "):
            VERSION = line.split("=", 1)[-1].replace('"', "").strip()
            break


with open("README.md") as fp:
    LONG_DESCRIPTION = fp.read()


# ==============================================================================
# FUNCTIONS
# ==============================================================================

short_description = "Functions is python for the most commun basic linear algebra operations."

setup(
    name="PyLABF",
    version=VERSION,
    description=short_description,
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Ferreira, Juan David",
    author_email="juandavid9a0@gmail.com",
    url="https://github.com/juniors90/PyLABF",
    packages=["pylabf"],
    license="The MIT License",
    install_requires=REQUIREMENTS,
    keywords=["pylabf"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "Topic :: Scientific/Engineering",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">= 3.8",
)