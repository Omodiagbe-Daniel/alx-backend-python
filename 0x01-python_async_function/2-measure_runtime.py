#!/usr/bin/env python3
"""
defines an async function measure_time with integers n
and max_delay as arguments
"""
import asyncio
from time import perf_counter
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """
        create a measure_time function with integers n and
        max_delay as arguments that measures the total execution
        for wait_n(n, max_max_delay) and returns total_time / n
    """
    start = perf_counter()
    asyncio.run(wait_n(n, max_delay))
    stop = perf_counter()
    return ((stop - start) / n)
