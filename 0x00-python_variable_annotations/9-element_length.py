#!/usr/bin/env python3
""" duck type an iterable object"""
from typing import Sequence, List, Tuple, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """annotated list"""

    return [Tuple[Sequence[i], int[len(i)]] for i in lst]
