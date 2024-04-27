#!/usr/bin/env python3
"""
takes a list of int and floats and returns their sum as float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """This function takes a list of int and floats
    and return the sum as float

    Argument:
    mxd_lst(list of int and floats): argument
    """
    return sum(mxd_lst)
