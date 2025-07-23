### JULY 4, 2025 -- P146: LRU CACHE ###

from collections import OrderedDict

class LRUCache:
    # using Ordered Dict for o(1) time
    def __init__(self, capacity: int):
        self._capacity = capacity
        self._cache = OrderedDict()
        
    def get(self, key: int) -> int:
        if key in self._cache:
            self._cache.move_to_end(key)
            return self._cache[key]
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self._cache:
            self._cache.move_to_end(key)
        self._cache[key] = value
        if len(self._cache) > self._capacity:
            self._cache.popitem(False)
