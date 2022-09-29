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
from pylabf.vector import (
    Vector,
    angle_between_vectors,
    area_of_parallelogram_spanned,
    area_of_triangle_spanned,
    cross_product,
    dot_product,
    get_parallel_projection,
    get_orthogonal_projection,
    is_orthogonal,
    is_parallel,
    minus,
    plus,
    times_scalar,
)

# ---------------------------------------------------------------------- #
# Initialize a some vectors                                              #
# ---------------------------------------------------------------------- #
vector1 = Vector([8.218, -9.341])
vector2 = Vector([7.119, 8.215])


# ---------------------------------------------------------------------- #
# Define a simple vector                                                 #
# ---------------------------------------------------------------------- #
print("Addition -> ", plus(vector1, vector2))
print("Difference -> ", minus(vector1, vector2))
print("The dot product -> ", dot_product(vector1, vector2))
print("The times scalar -> ", times_scalar(vector1, 20))
print(
    "Angle between vectors in Radian System-> ",
    angle_between_vectors(vector1, vector2),
)
print(
    "Angle between vectors in Sexagesimal System -> ",
    angle_between_vectors(vector1, vector2, sexagesimal=True),
)

# ---------------------------------------------------------------------- #
# This calculus exmaple explains how to find the vector projection of    #
# u = (3, 5) onto v = (2, 4) using the dot product and how to find the   #
# vector component of u orthogonal to v.  W1 is the component of u       #
# parallel to v and w2 is the component of u perpendicular to v.         #
# ---------------------------------------------------------------------- #
u = Vector([3, 5])
v = Vector([2, 4])
# 
print(u + v)
# Vector: (Decimal('5'), Decimal('9'))
print(u * v)
# 26
print("The parallel projection u onto v -> ", get_parallel_projection(u, v))
print(
    "The vector component of u orthogonal to v -> ",
    get_orthogonal_projection(u, v),
)


# ---------------------------------------------------------------------- #
# Define a simple vector in 3D                                           #
# ---------------------------------------------------------------------- #
vector1_in_3D = Vector([1.671, -1.012, -0.318])
vector2_in_3D = Vector([1.671, -1.012, -0.318])
vector3_in_3D = Vector([10, -13.012, 30.318])
print(
    "Area of parallelogram spanned -> ",
    area_of_parallelogram_spanned(vector1_in_3D, vector2_in_3D),
)
print(
    "The area of triangle spanned -> ",
    area_of_triangle_spanned(vector1_in_3D, vector3_in_3D),
)
print("The cross product -> ", cross_product(vector1_in_3D, vector3_in_3D))
print("Is orthogonal -> ", is_orthogonal(vector1_in_3D, vector3_in_3D))
print("Is parallel -> ", is_parallel(vector1_in_3D, vector3_in_3D))
print("Area of parallelogram spanned -> ", vector3_in_3D.magnitude)
