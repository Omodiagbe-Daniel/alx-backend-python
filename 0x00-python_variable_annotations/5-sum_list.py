#!/usr/bin/env python3
"""a function that takes a list of floats and return their sum"""
from typing import List

def sum_list(input_list: List[float]) -> float:
    """function takes a list of floats and return their sum"""
    sum: float = 0.0
    for i in input_list:
        sum += i
    return sum
