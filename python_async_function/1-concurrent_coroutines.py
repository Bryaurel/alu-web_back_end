#!/usr/bin/env python3
'''
Import wait_random from the previous python file that you’ve written
and write an async routine called wait_n that takes in 2 int arguments
'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''
    spawns wait_random n times with the specified max_delay
    returns a list of delays in ascending order without using sort()

    Args:
    n (int): The number of times to call wait_random
    max_delay (int): The maximum delay value passed to wait_random

    Returns:
    List[float]: List of float delays in ascending order
    '''
    # List comprehension to spawn n coroutines of wait_random concurrently
    tasks = [wait_random(max_delay) for _ in range(n)]

    # asyncio.gather to run them concurrently and collect the completed results
    delays = await asyncio.gather(*tasks)

    # Sort the delay manually using sorted()
    return sorted(delays)  # Sort the list manually without using sort()
