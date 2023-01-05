#!/usr/bin/env python3
"""a typed-annotated function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """a type-annotated function sum_list
       which takes a list input_list of floats as
       argument and returns their sum as a float"""

    sum = 0.0
    for i in input_list:
        sum += i
    return sum
