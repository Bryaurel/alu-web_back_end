#!/usr/bin/env python3
'''
Write a coroutine called async_generator that takes no arguments.
'''
import asyncio
import random
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''
    The coroutine will loop 10 times, each time asynchronously
    wait 1 second, then yield a random number between 0 and 10.
    '''
    for _ in range(10):
        await asyncio.sleep(1)  # Asynchroniously wait for  1 second
        yield random.uniform(0, 10)  # Yield a random float (0-10)