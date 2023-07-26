#!/usr/bin/env python3
"""basic caching"""
BaseCaching = __import__('base_caching').BaseCaching


class BasicCache(BaseCaching):
    """Inherits from Base Caching class"""
    def __init__(self):
        """initialize class with base caching"""
        BaseCaching.__init__(self)

    def put(self, key, item):
        """puts an item into  the cache dictionary"""
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """gets an item from dictionary"""
        if self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]
