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
            self.__dataset = dataset[1:]

        return self.__dataset

    def indexed_dataset(self) -> Dict[int, List]:
        """Dataset indexed by sorting position, starting at 0
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            truncated_dataset = dataset[:1000]
            self.__indexed_dataset = {
                i: dataset[i] for i in range(len(dataset))
            }
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = None, page_size: int = 10) -> Dict:
        """Provides a page of the dataset accounting for possible deletions."""
        assert isinstance(index, int) and index >= 0, (
            "Index must be a non-negative integer"
        )

        indexed_dataset = self.indexed_dataset()
        dataset_keys = sorted(indexed_dataset.keys())

        # Finding the closest valid index
        if index not in dataset_keys:
            valid_indices = [key for key in dataset_keys if key >= index]
            if not valid_indices:
                raise AssertionError("Index out of range")
            index = valid_indices[0]

        current_index = index
        data = []
        count = 0

        while count < page_size and current_index in dataset_keys:
            data.append(indexed_dataset[current_index])
            count += 1
            current_index += 1

        next_index = current_index if current_index in dataset_keys else None

        return {
            'index': index,
            'next_index': next_index,
            'page_size': len(data),
            'data': data
        }