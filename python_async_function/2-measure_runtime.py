#!/usr/bin/env python3
"""
measures the total execution time and return a float.
"""
import asyncio
import time
from typing import List
wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delay: int = 10) -> float:
    """
    This coroutine measures the total execution time for
    wait_n(n, max_delay) and returns total_time/n

    Arguments:
    n(int): number of times wait_random is called
    max_delay(int): max delay time for wait_random
    """
    start_time = time.time()
    await wait_n(n, max_delay)
    end_time = time.time()
    total_time = end_time - start_time
    return total_time / n
