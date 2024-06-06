#!/usr/bin/env python3
"""
to_kv: statically typed function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    k: string
    v: into or float
    return: tuple
    """
    sqrd = v**2
    return (k, sqrd)
