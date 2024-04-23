#!/usr/bin/env python3
"""
takes a list of int and floats and returns their sum as float.
"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    return sum(mxd_lst)
