#!/usr/bin/env python3
"""a type-annotated function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ type-annotated function make_multiplier that takes
        a float multiplier as argument and returns a function
        that multiplies a float by multiplier"""

    def make(num: float) -> float:
        """takes a float"""
        return num * multiplier

    return make
