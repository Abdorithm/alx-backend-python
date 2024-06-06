#!/usr/bin/env python3
"""
sum_list: statically typed function
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    input_list: given list of floats
    return: the sum of the list (float)
    """
    return sum(input_list)
