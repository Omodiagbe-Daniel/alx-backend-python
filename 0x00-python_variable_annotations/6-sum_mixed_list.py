#!/usr/bin/env python3
"""a type annotated function that takes a mixed list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """function takes a list of integers and floats and return their sum"""
    sum: float = 0.0
    for i in mxd_lst:
        sum += i
    return sum
