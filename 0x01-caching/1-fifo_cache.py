#!/usr/bin/env python3
"""
First In First Out Caching
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    inherits from BaseCaching 
    """
    def __init__(self):
        """
        initializing the cache
        """
        super().__init__()
        self.cache_data_list = []

    def put(self, key, item):
        """

        """
        if key and item:
            self.cache_data[key] = item
            self.cache_data_list.append(key)
        if len(self.cache_data_list) > BaseCaching.MAX_ITEMS:
            discardedData = self.cache_data_list.pop(0)
            print("DISCARD: {}".format(discardedData))

    def get(self, key):
        """ get key from the cache """
        if key in self.cache_data:
            return self.cache_data[key]
        return None
