#!/usr/bin/env python3
"""duck typing an iterable"""
from typing import Iterable, Sequence, Tuple, List


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    return [(i, len(i)) for i in lst]
