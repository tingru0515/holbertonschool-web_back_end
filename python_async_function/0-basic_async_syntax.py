#!/usr/bin/env python3
"""
takes an integer argument that waits for a ramdom delay seconds.
"""
import asyncio
import random


async def wait_random(max_delay: int =10) -> float:
    """This coroutine takes in an int argument (i.e. max_delay)
    and waits for a random delay between 0 and max_delay
    seconds and eventually returns it

    Argument:
    max_delay(int): argument
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
