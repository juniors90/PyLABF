#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file was part of Linear-Algebra-Basic-Functions and was modified.
# Copyright (c) 2016, Luis Espinosa de los Monteros. All rights reserved.
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

import math
from decimal import Decimal, getcontext
from string import ascii_lowercase

getcontext().prec = 30


CANNOT_NORMALIZE_ZERO_VECTOR_MSG = "Cannot normalize the zero vector"
NO_UNIQUE_PARALLEL_COMPONENT_MSG = "No unique parallel component"
NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG = "No unique orthogonal component"
RESULT_WAS_NOT_ORTOGONAL_AFTER_OPERATION_MSG = (
    "Result was not ortogonal after operation"
)
CROSS_PRODUCT_OPERATION_ONLY_FOR_3D_VECTORS_MSG = (
    "Cross product operation only for 3D vectors"
)


class Vector(object):
    def __init__(self, coordinates: list):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple([Decimal(x) for x in coordinates])
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError("The coordinates must be nonempty")

        except TypeError:
            raise TypeError("The coordinates must be an iterable")

    def __len__(self):
        return self.dimension

    def __str__(self):
        return "Vector: {}".format(self.coordinates)

    def __eq__(self, v: "Vector") -> "Vector":
        return self.coordinates == v.coordinates

    def __add__(self, vect: "Vector") -> "Vector":
        result = [
            v1 + v2 for v1, v2 in zip(self.coordinates, vect.coordinates)
        ]
        return type(self)(result)

    def __sub__(self, vect: "Vector") -> "Vector":
        result = [
            v1 - v2 for v1, v2 in zip(self.coordinates, vect.coordinates)
        ]
        return type(self)(result)

    def __mul__(self, other: "Vector") -> "Vector":
        if isinstance(other, list):
            vect = Vector(other)
            return sum(
                [v1 * v2 for v1, v2 in zip(vect.coordinates, self.coordinates)]
            )
        assert isinstance(other, type(self))
        return sum(
            [v1 * v2 for v1, v2 in zip(other.coordinates, self.coordinates)]
        )

    def __abs__(self) -> Decimal:
        sum_of_squares = sum(
            [Decimal(v) ** Decimal("2.0") for v in self.coordinates]
        )
        _magnitude = Decimal(math.sqrt(sum_of_squares))
        return _magnitude

    def __repr__(self):
        try:
            ll = [i for i in ascii_lowercase[8 : 8 + self.dimension]]
            list1 = [str(x) + y for x, y in zip(self.coordinates, ll)]
            return "+".join(list1)
        except Exception as e:
            raise e

    @property
    def unit_vector(self):
        try:
            c = Decimal("1.0") / self.magnitude
            return times_scalar(self, c)
        except ZeroDivisionError:
            raise Exception("Cannot normalize the zero vector")

    # def get_ortogonal(self):


def plus(vect1: Vector, vect2: Vector) -> Vector:
    result = [v1 + v2 for v1, v2 in zip(vect1.coordinates, vect2.coordinates)]
    return Vector(result)


def minus(vect1: Vector, vect2: Vector) -> Vector:
    result = [v1 - v2 for v1, v2 in zip(vect1.coordinates, vect2.coordinates)]
    return Vector(result)


# TypeError: can't multiply sequence by non-int of type 'decimal.Decimal'


def times_scalar(vector1: Vector, c) -> Vector:
    return Vector([c * v for v in vector1.coordinates])


def dot_product(vect1: Vector, vect2: Vector) -> Decimal:
    mult = [v1 * v2 for v1, v2 in zip(vect1.coordinates, vect2.coordinates)]
    return sum(mult)


def angle_between_vectors(
    vect1: Vector, vect2: Vector, sexagesimal: bool = None
) -> float:
    try:
        result = math.acos(
            dot_product(vect1, vect2) / (len(vect1) * len(vect2))
        )
        if sexagesimal:
            return (180 * result) / math.pi
        return result
    except Exception as e:
        raise e


def is_parallel(vect1: Vector, vect2: Vector, tolerance=None) -> bool:
    _tolerance = 1e-10 if tolerance is None else tolerance
    if (dot_product(vect1, vect1) < _tolerance) or (
        dot_product(vect2, vect2) < _tolerance
    ):
        return True
    result = True
    unit_v1 = vect1.unit_vector.coordinates
    unit_v2 = vect2.unit_vector.coordinates
    for v1, v2 in zip(unit_v1, unit_v2):
        result = result and (abs(round(v1, 10)) == abs(round(v2, 10)))
    return result


def is_orthogonal(vector1: Vector, vector2: Vector, tolerance=None) -> bool:
    _tolerance = 1e-10 if tolerance is None else tolerance
    return abs(dot_product(vector1, vector2)) < _tolerance


def get_parallel_projection(vect, basis):
    try:
        u = dot_product(vect, basis) / dot_product(basis, basis)
        return times_scalar(basis, u)
    except Exception as e:
        if str(e) == CANNOT_NORMALIZE_ZERO_VECTOR_MSG:
            raise Exception(NO_UNIQUE_PARALLEL_COMPONENT_MSG)
        else:
            raise e


def get_orthogonal_projection(vector: Vector, basis: Vector) -> Vector:
    try:
        projection = get_parallel_projection(vector, basis)
        return minus(vector, projection)
    except Exception as e:
        if str(e) == NO_UNIQUE_PARALLEL_COMPONENT_MSG:
            raise Exception(NO_UNIQUE_ORTHOGONAL_COMPONENT_MSG)
        else:
            raise e


def cross_product(vect1: Vector, vect2: Vector) -> Vector:
    try:
        if vect1.dimension == 3 and vect2.dimension == 3:
            x1, y1, z1 = vect1.coordinates
            x2, y2, z2 = vect2.coordinates
            x = (y1 * z2) - (y2 * z1)
            y = ((x1 * z2) - (x2 * z1)) * -1
            z = (x1 * y2) - (x2 * y1)
            cross_product = Vector([x, y, z])
            # Verifing that the answer is really ortogonal
            if is_orthogonal(vect1, cross_product) and is_orthogonal(
                vect1, cross_product
            ):
                return Vector([x, y, z])
            raise Exception(RESULT_WAS_NOT_ORTOGONAL_AFTER_OPERATION_MSG)
        raise Exception(CROSS_PRODUCT_OPERATION_ONLY_FOR_3D_VECTORS_MSG)
    except Exception as e:
        raise e


def area_of_parallelogram_spanned(vect1: Vector, vect2: Vector) -> Vector:
    return len(cross_product(vect1, vect2))


def area_of_triangle_spanned(vect1: Vector, vect2: Vector) -> Decimal:
    return len(cross_product(vect1, vect2)) / 2
