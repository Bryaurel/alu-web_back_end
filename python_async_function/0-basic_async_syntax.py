#!/usr/bin/env python3
'''
Write an asynchronous coroutine that takes in an integer argument
'''
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    '''
    waits for a random delay between 0 and max_delay seconds
    and returns the delay.

    Args:
    max_delay (int): Maximum delay in seconds. Default is 10.

    Returns:
    float: The actual delay.
    '''
    delay = random.uniform(0, max_delay)
    # Generate a random float between 0 and max_delay
    await asyncio.sleep(delay)
    # Pause execution for the generated delay
    return delay
