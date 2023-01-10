#!/usr/bin/env python3
"""
defines a function task_wait_n identical to wait_n
"""
import asyncio
from typing import List
task_wait_random = __import__("3-tasks").task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
        write an async routine called wait_n that takes in 2 int arguments
        (in this order): n and max_delay You will spawn
        wait_random n times with the specified max_delay
        wait_n should return the list of all the delays (float values)
    """
    tasks = []
    for i in range(n):
        task = await (task_wait_random(max_delay))
        tasks.append(task)
    return sorted(tasks)
