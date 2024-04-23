#!/usr/bin/env python3
"""
Asynchronous routine that spawns wait_random n times with
the specified max_delay.
Returns a list of all the delays in ascending order.
"""
import asyncio
from typing import List


wait_random = __import__('0-basic_async_syntax').wait_random

async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    delays = []
    tasks = []

    for _ in range(n):
        task = wait_random(max_delay)
        tasks.append(task)

    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays
