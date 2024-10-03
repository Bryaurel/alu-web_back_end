#!/usr/bin/env python3
'''
type-annotated function floor which takes a float n as argument
and returns the floor of the float.
'''
import math


def floor(n: float) -> int:
    # return the floor of the float
    '''
    The floor is the largest integer less or equal to the given float n
    The floor value should always be an integer 'int'
    '''
    return math.floor(n)
