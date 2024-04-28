#!/usr/bin/env python3
"""
execute async_comprehension four times in parallel,
measure the total runtime and return it.
"""
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """This coroutine will execute async_comprehension
    four times in parallel using asyncio.gather
    """
    start_time = asyncio.get_event_loop().time()
    await asyncio.gather(*[async_comprehension() for _ in range(4)])
    end_time = asyncio.get_event_loop().time()
    return end_time - start_time
