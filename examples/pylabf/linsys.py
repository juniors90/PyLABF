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
from pylabf.linsys import LinearSystem, MyDecimal
from pylabf.plane import Plane
from pylabf.vector import Vector, is_parallel

# ---------------------------------------------------------------------- #
# Initialize a some vectors                                              #
# ---------------------------------------------------------------------- #

p0 = Plane(["1", "1", "1"], constant_term="1")
p1 = Plane(["0", "1", "0"], constant_term="2")
p2 = Plane(["1", "1", "-1"], constant_term="3")
p3 = Plane(["1", "0", "-2"], constant_term="2")

s = LinearSystem([p0, p1, p2, p3])

print("# Linear System Test 1")
print(s.indices_of_first_nonzero_terms_in_each_row())
print("{}, {}, {}, {}".format(s[0], s[1], s[2], s[3]))
print(len(s))
print(s)
s[0] = p1
print(s)

print(MyDecimal("1e-9").is_near_zero())
print(MyDecimal("1e-11").is_near_zero())

print("# Linear System Test 2")

p1 = Plane(normal_vector=["1", "1", "1"], constant_term="1")
p2 = Plane(normal_vector=["0", "1", "1"], constant_term="2")
s = LinearSystem([p1, p2])
t = s.compute_triangular_form()
print(t)
if not (t[0] == p1 and t[1] == p2):
    print("test case 1 failed")

print("# Linear System Test 3")

p1 = Plane(normal_vector=["0", "1", "1"], constant_term="1")
p2 = Plane(normal_vector=["1", "-1", "1"], constant_term="2")
p3 = Plane(normal_vector=["1", "2", "-5"], constant_term="3")
s = LinearSystem([p1, p2, p3])
t = s.compute_triangular_form()
print(t)
if not (
    t[0] == Plane(normal_vector=["1", "-1", "1"], constant_term="2")
    and t[1] == Plane(normal_vector=["0", "1", "1"], constant_term="1")
    and t[2] == Plane(normal_vector=["0", "0", "-9"], constant_term="-2")
):
    print("test case 3 failed")

print("# Linear System Test 4")

p1 = Plane(normal_vector=["1", "1", "1"], constant_term="1")
p2 = Plane(normal_vector=["0", "1", "0"], constant_term="2")
p3 = Plane(normal_vector=["1", "1", "-1"], constant_term="3")
p4 = Plane(normal_vector=["1", "0", "-2"], constant_term="2")
s = LinearSystem([p1, p2, p3, p4])
t = s.compute_triangular_form()
print(t)
if not (
    t[0] == Plane(normal_vector=["1", "1", "1"], constant_term="1")
    and t[1] == Plane(normal_vector=["0", "1", "0"], constant_term="2")
    and t[2] == Plane(normal_vector=["1", "1", "-1"], constant_term="3")
    and t[3] == Plane(normal_vector=["1", "0", "-2"], constant_term="2")
):
    print("test case 4 failed")


print("# Linear System Test 5")

p1 = Plane(normal_vector=["1", "1", "1"], constant_term="1")
p2 = Plane(normal_vector=["1", "1", "1"], constant_term="2")
s = LinearSystem([p1, p2])
t = s.compute_triangular_form()
if not (t[0] == p1):
    print("test case 5 failed")
