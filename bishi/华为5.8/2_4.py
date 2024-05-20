
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.usage_count = {}
        self.timestamp = 0

    def write(self, local_cell: int, neighbor_cell: int):
        if local_cell in self.cache:
            self.cache.move_to_end(local_cell)
            self.cache[local_cell] = (neighbor_cell, self.timestamp)
            self.usage_count[local_cell] += 1
        else:
            if len(self.cache) >= self.capacity:
                least_used = min(self.usage_count.items(), key=lambda x: (x[1], self.cache[x[0]][1]))
                del self.cache[least_used[0]]
                del self.usage_count[least_used[0]]
            self.cache[local_cell] = (neighbor_cell, self.timestamp)
            self.usage_count[local_cell] = 1
        self.timestamp += 1

    def read(self, local_cell: int):
        if local_cell in self.cache:
            self.cache.move_to_end(local_cell)
            self.cache[local_cell] = (self.cache[local_cell][0], self.timestamp)
            self.usage_count[local_cell] += 1
            self.timestamp += 1
        else:
            pass 

    def query(self, local_cell: int):
        if local_cell in self.cache:
            return self.cache[local_cell][0]
        else:
            return -1

def solve():
    lru_cache = None
    while True:
        try:
            x = input()
            if x == "capacity:":
                capacity = int(input())
                lru_cache = LRUCache(capacity)
            elif x == "write:":
                cnt = int(input())
                for _ in range(cnt):
                    local_cell, neighbor_cell = map(int, input().split())
                    lru_cache.write(local_cell, neighbor_cell)
            elif x == "read:":
                local_cell = int(input())
                lru_cache.read(local_cell)
            elif x == "query:":
                local_cell = int(input())
                result = lru_cache.query(local_cell)
                print(result)           
        except:
            break
solve()

