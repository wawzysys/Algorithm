from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity
    def query(self, key: int):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return None

    def insert(self, key: int):
        if key in self.cache:
            self.cache.move_to_end(key)
        else:
            if len(self.cache) >= self.capacity:
                self.cache.popitem(last=False)
            self.cache[key] = None

    def delete(self, key: int):
        if key in self.cache:
            del self.cache[key]

def lru_cache_operations(capacity: int, operations: list):
    lru_cache = LRUCache(capacity)
    for op in operations:
        action, key = op.split()
        key = int(key)
        if action == 'Q':
            lru_cache.query(key)
        elif action == 'A':
            lru_cache.insert(key)
        elif action == 'D':
            lru_cache.delete(key)
    return sorted(lru_cache.cache.keys())

c, m  = map(int, input().split())
operations = [input() for _ in range(m)]

result = lru_cache_operations(c, operations)
print(*result)  
