#!/usr/bin/env python3
"""
a coroutine measure_time that imports
async_comprehension
"""
from asyncio import gather, run
from time import perf_counter as pf
async_com = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """
        Import async_comprehension from the previous file and
        write a measure_runtime coroutine that will execute
        async_comprehension four times in parallel using asyncio.gather
        measure_runtime should measure the total runtime and return it
    """

    start = pf()
    await (gather(async_com(), async_com(), async_com(), async_com()))
    stop = pf()
    return stop - start
