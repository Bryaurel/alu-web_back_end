#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination
"""

import csv
import math
from typing import List, Dict


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None
        self.__indexed_dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]  # Skip the header

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {
                i: dataset[i]
                for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """
        Deletion-resilient hypermedia pagination method.
        """
        # Get the indexed dataset
        indexed_data = self.indexed_dataset()

        # Ensure index is a valid integer within range
        assert isinstance(index, int) and 0 <= index < len(self.dataset()), \
            "Index out of range"

        # Initialize data for pagination
        data = []
        current_index = index
        next_index = index

        # Loop through the indexed dataset and collect data for the page
        while len(data) < page_size and next_index < len(self.dataset()):
            if next_index in indexed_data:
                data.append(indexed_data[next_index])
            next_index += 1

        # Return the required pagination dictionary
        return {
            "index": index,
            "next_index": next_index,
            "page_size": len(data),
            "data": data
        }
