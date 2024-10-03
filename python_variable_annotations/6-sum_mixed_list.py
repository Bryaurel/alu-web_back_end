#!/usr/bin/env python3
'''
type-annotated function sum_mixed_list which takes a list mxd_lst
of integers and floats and returns their sum as a float.
'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    return the sum of a mixed list of integers and floats
    sum_mixed_list is the function name

    Union is used to indicate that the list can contain either int or float types.
    '''
    return float(sum(mxd_lst))
