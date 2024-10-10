#!/usr/bin/env python3
'''
Annotate the function’s parameters
and return values with the appropriate types
'''
from typing import List, Tuple, Iterable, Sequence

def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    Takes an iterable of sequences and returns a list of tuples,
    where each tuple contains a sequence and its length.
    
    Args:
    lst (Iterable[Sequence]): An iterable (e.g., list, tuple)
    of sequences (e.g., string, list, tuple).
    
    Returns:
    List[Tuple[Sequence, int]]: A list of tuples
    with a sequence and its corresponding length.
    '''
    return [(i, len(i)) for i in lst]
