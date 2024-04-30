#!/usr/bin/env python3
"""This module defines index_range function and Server class"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end indices for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index


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
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """Retrieve a specific page of data from the dataset."""
        assert (isinstance(page, int) and isinstance(page_size, int)
                and page > 0 and page_size > 0)
        if self.__dataset is None:
            self.dataset()
        pagination: Tuple[int, int] = index_range(page, page_size)
        return [each_page
                for each_page in self.__dataset[pagination[0]:pagination[1]]]
    