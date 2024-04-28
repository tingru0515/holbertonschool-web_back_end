#!/usr/bin/env python3
"""write a coroutine collect 10 random numbers usingan async
comprehensing then return the 10 random numbers.
"""
import asyncio
import random
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """This coroutine collect 10 random numbers
    using an async comprehensing over async_generator
    then return the 10 random numbers
    """
    return [i async for i in async_generator()]
