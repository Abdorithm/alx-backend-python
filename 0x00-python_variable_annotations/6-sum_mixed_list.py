#!/usr/bin/env python3
"""
sum_mixed_list: statically typed function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """
    mxd_lst: list of integers and float numbers
    return: their sum (float)
    """
    return sum(mxd_lst)
