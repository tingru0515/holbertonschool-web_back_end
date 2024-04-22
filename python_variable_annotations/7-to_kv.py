#!/usr/bin/python3
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    takes a string and an int or float as arguments and returns a tuple.
    """
    return k, v**2
