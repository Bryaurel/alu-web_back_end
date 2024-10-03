#!/usr/bin/env python3
'''
 type-annotated function to_kv that takes a string k and an int OR float v
 as arguments and returns a tuple. The first element of the tuple is the string k.
 The second element is the square of the int/float v and should be annotated as a float.
 '''
 from typing import Union, Tuple


 def to_kv(k: str, v:Union[int, float]) -> Tuple[str, float]:
    # Union can stand for "Or"
    '''
    return a tuple from a string or the square of a number

    Args:
    k (str): A string key
    v(Union[int, float]): An integer or float value
    '''
    return (k, float(v ** 2))   # "** 2" expresses the square
