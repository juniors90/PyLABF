#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# This file is part of the
#     PyLABF Project (https://github.com/juniors90/PyLABF/).
# Copyright (c) 2022, Ferreira Juan David
# License: MIT
# Full Text:
#    https://github.com/juniors90/PyLABF/blob/master/LICENSE

"""PyLABF

Functions is python for the most commun basic linear algebra operations.
"""

# =============================================================================
# IMPORTS
# =============================================================================

import os
import pathlib
import sys

# this path is pointing to project/docs/source
CURRENT_PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
PYLABF_PATH = CURRENT_PATH.parent.parent

sys.path.insert(0, str(PYLABF_PATH))

# ====================================================
from decimal import Decimal
from pylabf.plane import Plane
from pylabf.vector import Vector, is_parallel

# ---------------------------------------------------------------------- #
# Initialize a some vectors                                              #
# ---------------------------------------------------------------------- #

planeA1 = Plane([Decimal(4.046), Decimal(2.836)], 1.21)
planeA2 = Plane([Decimal(10.115), Decimal(7.09)], 3.025)

planeB1 = Plane([Decimal(7.204), Decimal(3.182)], 8.68)
planeB2 = Plane([Decimal(8.172), Decimal(4.114)], 9.883)

planeC1 = Plane([Decimal(1.182), Decimal(5.562)], 6.744)
planeC2 = Plane([Decimal(1.773), Decimal(8.343)], 9.525)

print("A Plane")
same_plane = planeA1.__eq__(planeA2)
print("Are the same plane?: %s" % same_plane)
if not same_plane:
    parallel = is_parallel(planeA1.normal_vector, planeA2.normal_vector)
    print("Are Parallel?: %s" % parallel)

print("B Plane")
same_plane = planeB1.__eq__(planeB2)
print("Are the same plane?: %s" % same_plane)
if not same_plane:
    parallel = is_parallel(planeB1.normal_vector, planeB2.normal_vector)
    print("Are Parallel?: %s" % parallel)

print("C Plane")
same_plane = planeC1.__eq__(planeC2)
print("Are the same plane?: %s" % same_plane)
if not same_plane:
    parallel = is_parallel(planeC1.normal_vector, planeC2.normal_vector)
    print("Are Parallel?: %s" % parallel)
