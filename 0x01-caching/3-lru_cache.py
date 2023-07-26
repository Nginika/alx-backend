#!/usr/bin/env python3
"""class of caching system using LRU algorithm"""
from typing import OrderedDict
BaseCaching = __import__('base_caching').BaseCaching


class LRUCache(BaseCaching):
    """class inheriting from base caching"""
    def __init__(self):
        """base caching init inheritance"""
        BaseCaching.__init__(self)
        super().__init__()
        self.lru_order = OrderedDict()

    def put(self, key, item):
        """implements adding item to cache"""
        if key and item:
            self.lru_order[key] = item
            self.lru_order.move_to_end(key)
            self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            item_discarded = next(iter(self.lru_order))
            del self.cache_data[item_discarded]
            print("DISCARD:", item_discarded)

        if len(self.lru_order) > BaseCaching.MAX_ITEMS:
            self.lru_order.popitem(last=False)

    def get(self, key):
        """implements get items from cache"""
        if self.cache_data.get(key) is None:
            return None
        else:
            self.lru_order.move_to_end(key)
            return self.cache_data[key]
