#!/usr/bin/env python3
"""
safe_first_element: statically typed function
"""
from typing import Sequence, Any, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    lst: Sequence[Any]

    return: Union of Any and None
    """
    if lst:
        return lst[0]
    else:
        return None
