#!/usr/bin/env python3
"""
takes a string and an int or float as arguments and returns a tuple.
"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """This function takes a string and int/float and return a tuple.
    First element of tuple being string k
    Second element of tuple being square of the int/float v

    Arguments:
    k(str): first argument
    v(int or float): second argument
    """
    return k, v**2
