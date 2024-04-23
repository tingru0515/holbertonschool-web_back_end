#!/usr/bin/env python3
"""
takes an integer argument that waits for a ramdom delay seconds.
"""
import asyncio
import random


async def wait_random(max_delay=10):
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
