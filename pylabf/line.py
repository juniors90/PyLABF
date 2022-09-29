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

from decimal import Decimal, getcontext

from .linsys import MyDecimal
from .vector import Vector, is_parallel, is_orthogonal, minus


getcontext().prec = 30


class Line(object):

    NO_NONZERO_ELTS_FOUND_MSG = "No nonzero elements found"
    THEY_ARE_PARALLEL_AND_DONT_INTERSECT_MSG = (
        "They are parallel and never intersect."
    )
    THEY_ARE_THE_SAME_LINE_MSG = (
        "Has infinite intersections because they are the same line."
    )

    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

        if not normal_vector:
            all_zeros = ["0"] * self.dimension
            normal_vector = all_zeros

        self.normal_vector = (
            Vector(normal_vector)
            if isinstance(normal_vector, list)
            else normal_vector
        )

        if not constant_term:
            constant_term = Decimal("0")

        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def set_basepoint(self):
        try:
            n = self.normal_vector.coordinates
            c = self.constant_term
            basepoint_coords = ["0"] * self.dimension

            initial_index = Line.first_nonzero_index(n)
            initial_coefficient = n[initial_index]

            basepoint_coords[initial_index] = c / initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except Exception as e:
            if str(e) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise e

    def __eq__(self, l):
        if is_parallel(self.normal_vector, l.normal_vector):
            direction_vector = minus(self.basepoint, l.basepoint)
            return is_orthogonal(direction_vector, self.normal_vector)
        return False

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ""

            if coefficient < 0:
                output += "-"
            if coefficient > 0 and not is_initial_term:
                output += "+"

            if not is_initial_term:
                output += " "

            if abs(coefficient) != 1:
                output += "{}".format(abs(coefficient))

            return output

        n = self.normal_vector.coordinates

        try:
            initial_index = Line.first_nonzero_index(n)
            terms = [
                write_coefficient(n[i], is_initial_term=(i == initial_index))
                + "x_{}".format(i + 1)
                for i in range(self.dimension)
                if round(n[i], num_decimal_places) != 0
            ]
            output = " ".join(terms)

        except Exception as e:
            if str(e) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = "0"
            else:
                raise e

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += " = {}".format(constant)

        return output

    @staticmethod
    def first_nonzero_index(iterable):
        for k, item in enumerate(iterable):
            if not MyDecimal(item).is_near_zero():
                return k
        raise Exception(Line.NO_NONZERO_ELTS_FOUND_MSG)


def intersection(vect1: Vector, vect2: Vector) -> Vector:
    if vect1.__eq__(vect2):
        return vect1
    if is_parallel(vect1.normal_vector, vect2.normal_vector):
        return None
    A, B = vect1.normal_vector.coordinates
    C, D = vect2.normal_vector.coordinates
    k1 = vect1.constant_term
    k2 = vect2.constant_term
    x = (D * k1 - B * k2) / (A * D - B * C)
    y = (A * k2 - C * k1) / (A * D - B * C)
    return Vector([x, y])
