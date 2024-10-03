#!/usr/bin/env python3
'''
type-annotated function make_multiplier that takes a float multiplier
as argument and returns a function that multiplies a float by multiplier
'''
from typing import Callable
# Callable is a type hint that indicates that an object
# can be called like a function


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    Create a multiplier
    Callable[[float], float]: A function that multiplies a float by the multiplier
    '''
    def multiplier_function(value: float) -> float:
        '''
        Create a multiplier function
        '''
        return value * multiplier

    return multiplier_function
