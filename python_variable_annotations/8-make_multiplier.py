#!/usr/bin/env python3
"""
takes a float as argument and returns a function that
multiplies a float.
"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    This function takes a float(i.e. multiplier) as argument
    and return a function that multiplies a float by multiplier

    Argument
    multipler(float): argument
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
