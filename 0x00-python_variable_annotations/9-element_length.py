#!/usr/bin/env python3
"""
element_length: statically typed function
"""
from typing import List, Iterable, Sequence, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    lst: iterable sequence

    return: list of tuples
    """
    return [(i, len(i)) for i in lst]
