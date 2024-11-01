#!/usr/bin/env python3
"""a type annotated function that takes a mixed list"""
from typing import List


def sum_mixed_list(mxd_lst: List[int | float]) -> float:
    """function takes a list of integers and floats and return their sum"""
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
