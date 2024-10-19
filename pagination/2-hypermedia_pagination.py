#!/usr/bin/env python3
'''
Replicate index_range from the previous task and implement get_hyper method.
'''

import csv
import math
from typing import List, Dict


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
        assert isinstance(page, int) and page > 0, \
            "page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0, \
            "page_size must be a positive integer"

        # Get the start and end index for the pagination
        start_index, end_index = index_range(page, page_size)

        # Fetch the dataset
        data = self.dataset()

        # Return the appropriate slice of data
        if start_index >= len(data):
            return []

        return data[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Get paginated data along with hypermedia pagination info.
        """
        # Get the paginated page data
        data = self.get_page(page, page_size)

        # Calculate total number of pages
        dataset_len = len(self.dataset())
        total_pages = math.ceil(dataset_len / page_size)

        # Determine the next and previous pages
        next_page = page + 1 if page < total_pages else None
        prev_page = page - 1 if page > 1 else None

        # Build the result dictionary
        hypermedia = {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": next_page,
            "prev_page": prev_page,
            "total_pages": total_pages
        }

        return hypermedia
