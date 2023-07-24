#!/usr/bin/env python3
"""function named index_range that takes two integer arguments
page and page_size.
another get_page function that gets data for the index ranges
class that reads data from a file.
"""
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> tuple:
    """returns index range in a page"""
    x = (page - 1) * page_size
    y = page * page_size
    list_range = (x, y)
    return list_range


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """init class"""
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
        """get page using index range"""
        assert (type(page) == int)
        assert (page > 0)
        assert (type(page_size) == int)
        assert (page_size > 0)
        list_range = index_range(page, page_size)
        if list_range[0] >= len(self.dataset()):
            return []
        return self.dataset()[list_range[0]:list_range[1]]
