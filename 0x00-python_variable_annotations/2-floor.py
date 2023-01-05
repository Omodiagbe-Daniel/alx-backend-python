#!/usr/bin/env python3
"""a type-annotated function floor"""
from math import floor as fr


def floor(n: float) -> int:
    """ a type-annotated function concat that takes a float
        n as arguments and
        returns the floor of the float"""

    return fr(n)
