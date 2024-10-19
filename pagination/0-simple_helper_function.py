#!/usr/bin/env python3
'''
Write a function named index_range
that takes two integer arguments page and page_size
'''


def index_range(page: int, page_size: int) -> tuple:
    '''
    Return a tuple containing the start index and end index
    for the given page and page_size.
    '''
    if page < 1 or page_size < 1:
        raise ValueError("Both page and page_size must be greater than 0")

    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)
