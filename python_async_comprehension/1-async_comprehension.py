#!/usr/bin/env python3
'''
Import async_generator from the previous task
and then write a coroutine called async_comprehension
that takes no arguments.
'''
import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Collects 10 random numbers using an async comprehension
    over async_generator and returns them as a list.
    '''
    return [number async for number in async_generator()]
