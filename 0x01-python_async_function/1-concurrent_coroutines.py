#!/usr/bin/env python3
"""
defines an async function wait_random
that takes 2 arguments n and max_delay
"""
import asyncio
from typing import List
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
        write an async routine called wait_n that takes in 2 int arguments
        (in this order): n and max_delay You will spawn
        wait_random n times with the specified max_delay
        wait_n should return the list of all the delays (float values)
    """
    tasks = []
    for i in range(n):
        tasks.append(asyncio.create_task(wait_random(max_delay)))
    return [await task for task in asyncio.as_completed(tasks)]
