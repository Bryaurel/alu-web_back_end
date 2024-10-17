#!/usr/bin/env python3
'''
Import async_comprehension from the previous file
and write a measure_runtime coroutine that will execute
async_comprehension four times in parallel using asyncio.gather.
'''
import asyncio
from time import time

async_comprehension = __import__(1-async_comprehension).async_comprehension


async def measure_runtime() -> float:
    '''
    Run async_comprehension 4 times in parallel
    '''
    start = time()
    await asyncio.gather(
        async_comprehension(),
        async_comprehension(),
        async_comprehension(),
        async_comprehension()
    )

    end_time = time()  # End the timer

    return end - start
