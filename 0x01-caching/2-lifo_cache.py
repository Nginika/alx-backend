#!/usr/bin/env python3
"""creating a caching system using LIFO algorithm"""
BaseCaching = __import__('base_caching').BaseCaching


class LIFOCache(BaseCaching):
    """class inherited from base caching"""
    def __init__(self):
        """initialize LIFOCache with Basecaching init"""
        BaseCaching.__init__(self)
        super().__init__()

    def put(self, key, item):
        """implements adding to the cache with LIFO algorithm"""
        if key and item:
            self.cache_data[key] = item
            if (len(self.cache_data) > BaseCaching.MAX_ITEMS):
                last_in = list(self.cache_data)[-2]
                print('DISCARD: {0}'.format(last_in))
                self.cache_data.pop(last_in)

    def get(self, key):
        """implements get items from cache"""
        if self.cache_data.get(key) is None:
            return None
        else:
            return self.cache_data[key]
