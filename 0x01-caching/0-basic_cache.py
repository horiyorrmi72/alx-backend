#!/usr/bin/env python3
"""
A Basic Cache
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache class that inherits from base_caching system
    """
    def __init__(self):
        """
        initializing the class
        """
        super().__init__()
        self.cache_data = {}

    def put(self, key, item):
        """
        assign to the dictionary self.cache_data
        the item value for the key key.
        If key or item is None, this method should not do anything
        """
        if key and item:
            self.cache_data[key] = item
        else:
            pass

    def get(self, key):
        """
        return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None
        """
        if key in self.cache_data:
            return self.cache_data[key]
        else:
            return None
