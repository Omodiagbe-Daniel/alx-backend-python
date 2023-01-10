#!/usr/bin/env python3
"""
defines a coroutine async_comprehension
that takes no arguments
"""
import asyncio
import typing
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension():
    """
        an async function that imports async_generator
        collects 10 random numbers using async comprehension
        over async_generator and then return the 10 random numbers
    """

    async_list = [x async for x in async_generator()]
    return async_list
