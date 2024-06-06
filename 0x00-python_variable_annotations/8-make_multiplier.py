#!/usr/bin/env python3
"""
make_multiplier: statically typed function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    multiplier: float number
    return: another function that does the
    multiplication
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
