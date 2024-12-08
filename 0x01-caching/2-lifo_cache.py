#!/usr/bin/env python3
"""
Last In First Out caching
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    Inherit from BaseCaching
    """
    def __init__(self):
        """
        Initializing the cache
        """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """
        Assigning key and item
        if key or item is None, this method should not do anything.
        If the number of items in self.cache_data is higher
        that BaseCaching.MAX_ITEMS:
        you must discard the last item put in cache (LIFO algorithm)
        """
        if len(self.cache_data) == self.MAX_ITEMS and key not in self.stack:
            discardData = self.stack.pop()
            del self.cache_data[discardData]
            print("DISCARD: {}".format(discardData))
        if key and item:
            self.stack.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Fetching  data with key
        Must return the value in self.cache_data linked to key.
        If key is None or if the key doesn’t exist in self.cache_data,
        return None
        """
        if not key or key not in self.cache_data.keys():
            return None
        return self.cache_data.get(key)
