#!/usr/bin/env python3
"""
a coroutine measure_time that imports
async_comprehension
"""
from asyncio import gather, run
from time import perf_counter as pf
async_com = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    start = pf()
    await (gather(async_com(), async_com(), async_com(), async_com()))
    stop = pf()
    return stop - start
