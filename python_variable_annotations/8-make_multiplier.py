#!/usr/bin/python3
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    takes a float as argument and returns a function that
    multiplies a float.
    """
    def multiply(x: float) -> float:
        return x * multiplier
    return multiply
