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
from pylabf.line import Line, intersection
from pylabf.vector import Vector, is_parallel

# ---------------------------------------------------------------------- #
# Initialize a some vectors                                              #
# ---------------------------------------------------------------------- #
vector1 = Vector([8.218, -9.341])

lineA1 = Line(vector1, 1.21)
lineA2 = Line([Decimal(10.115), Decimal(7.09)], 3.025)

print(lineA1)
print(lineA2)

lineB1 = Line([Decimal(7.204), Decimal(3.182)], 8.68)
lineB2 = Line([Decimal(8.172), Decimal(4.114)], 9.883)

lineC1 = Line([Decimal(1.182), Decimal(5.562)], 6.744)
lineC2 = Line([Decimal(1.773), Decimal(8.343)], 9.525)

print("A Line")

same_line = lineA1.__eq__(lineA2)

print(f"Are the same line?: {same_line }")

if not same_line:
    parallel = is_parallel(lineA1.normal_vector, lineA2.normal_vector)
    print(f"Are paralell?: {parallel}")
    if not parallel:
        print(f"Intersection:  {intersection(lineA1, lineA2)}")

print("B Line")

same_line = lineB1.__eq__(lineB2)

print("Are the same line?: {same_line}")

if not same_line:
    parallel = is_parallel(lineB1.normal_vector, lineB2.normal_vector)
    print("Are Parallel?: %s" % parallel)
    if not parallel:
        print("Intersection: %s" % intersection(lineB1, lineB2))

print("C Line")

same_line = lineC1.__eq__(lineC2)

print("Are the same line?: %s" % same_line)

if not same_line:
    parallel = is_parallel(lineC1.normal_vector, lineC2.normal_vector)
    print("Are Parallel?: %s" % parallel)
    if not parallel:
        print("Intersection: %s" % intersection(lineC1, lineC2))
