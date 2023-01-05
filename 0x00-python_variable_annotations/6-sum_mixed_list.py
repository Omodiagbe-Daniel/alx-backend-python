#!/usr/bin/env python3
"""a typed-annotated function sum_mixed_list"""
from typing import Union


def sum_mixed_list(mxd_lst: Union[int, float]) -> float:
    """a type-annotated function sum_mixed_list
       which takes a list mxd_lst of integers and
       floats and returns their sum as a float"""

    sum = 0.0
    for i in mxd_lst:
        sum += i
    return sum
