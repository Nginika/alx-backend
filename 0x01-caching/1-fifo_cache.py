#!/usr/bin/python3
"""A first in first out cache class"""
BaseCaching = __import__('base_caching').BaseCaching


class FIFOCache(BaseCaching):
    def __init__(self):
        """initialize with basecaching class"""
        BaseCaching.__init__(self)
        super().__init__()

    def put(self, key, item):
        """implements put to cache with FIFO alorithm"""
        if key and item:
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                first_in = list(self.cache_data)[0]
                print('DISCARD: {0}'.format(first_in))
                self.cache_data.pop(first_in)

    def get(self, key):
        """implements get items from cache"""
        if self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]
