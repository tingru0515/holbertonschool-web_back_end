#!/usr/bin/env python3
"""
takes a string and an int or float as arguments and returns a tuple.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    return k, v**2
