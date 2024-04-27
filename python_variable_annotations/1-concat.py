#!/usr/bin/env python3
"""
takes two strings as input and returns a string.
"""


def concat(str1: str, str2: str) -> str:
    """This function returns a concatenated string by taking 2 str arguments

    Arguments:
    str1(str): First string
    str2(str): Second string
    """
    return "{}{}".format(str1, str2)
