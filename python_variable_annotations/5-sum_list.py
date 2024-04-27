#!/usr/bin/env python3
"""
takes a list of floats and return sum as float.
"""


from typing import List


def sum_list(input_list: List[float]) -> float:
    """This function takes a list of floats as arguments
    and return their sum as a float

    Argument:
    input_list(list of floats): argument
    """
    return sum(input_list)
