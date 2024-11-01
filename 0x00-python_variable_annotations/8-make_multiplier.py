#!/usr/bin/env python3
"""a type annotated function called make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """a type-annotated function make_multiplier that takes
    a float multiplier as argument and returns a function
    that multiplies a float by multiplier"""
    def mul(val: float) -> float:
        """returns a float"""
        return val * multiplier
    return mul
