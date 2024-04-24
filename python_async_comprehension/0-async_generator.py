#!/usr/bin/env python3
"""
the coroutine will loop 10 times, each time asynchronously
wait 1 second then yield a random number.
"""
import asyncio
import random


async def async_generator():
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
