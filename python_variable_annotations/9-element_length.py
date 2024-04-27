#!/usr/bin/env python3
"""
annotates parameters and return values of the function.
"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """This function return a list

    Argument
    lst(list): list argument"""
    return [(i, len(i)) for i in lst]
