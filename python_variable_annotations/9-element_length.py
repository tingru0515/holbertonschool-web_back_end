#!/usr/bin/python3
from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """
    annotates parameters and return values of the function.
    """
    return [(i, len(i)) for i in lst]
