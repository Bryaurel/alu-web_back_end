#!/usr/bin/env python3
'''
Copy index_range from the previous task
'''

import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    '''
    Return a tuple containing the start index and end index
    for the given page and page_size.
    '''
    start_index = (page - 1) * page_size
    end_index = start_index + page_size

    return (start_index, end_index)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Get the correct page from the dataset based on page and page_size.
        """
        # Ensure that page and page_size are valid integers greater than 0
        assert isinstance(page, int) and page > 0,
        assert isinstance(page_size, int) and page_size > 0,

        # Get the start and end index for the pagination
        start_index, end_index = index_range(page, page_size)

        # Fetch the dataset
        data = self.dataset()

        # Return the appropriate slice of data
        if start_index >= len(data):
            return []

        return data[start_index:end_index]
