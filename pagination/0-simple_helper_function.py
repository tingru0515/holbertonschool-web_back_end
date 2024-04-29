#!/usr/bin/env python3
"""return a tuple of size two containing a start index and an end index"""
def index_range(page: int, page_size: int) -> tuple:
    """
    Return a tuple of start and end indices for a given page and page size.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return start_index, end_index
