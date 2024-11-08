import heapq
import time

class NeighborCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  
        self.access_count = {}  
        self.access_time = {}  
        self.timestamp = 0  
    def write(self, x, y):
        if x in self.cache:
            self.cache[x] = y
            self.access_count[x] += 1
            self.access_time[x] = self.timestamp
        else:
            if len(self.cache) >= self.capacity:
                self.evict() 
            self.cache[x] = y
            self.access_count[x] = 1
            self.access_time[x] = self.timestamp

    def evict(self):
        min_heap = [(self.access_count[key], self.access_time[key], key) for key in self.cache]
        _, _, least_used_cell = heapq.nsmallest(1, min_heap)[0]

        del self.cache[least_used_cell]
        del self.access_count[least_used_cell]
        del self.access_time[least_used_cell]

    def read(self, x):
        if x in self.cache:
            self.access_count[x] += 1
            self.access_time[x] = self.timestamp
            return self.cache[x]
        else:
            return None

    def query(self, x):
        if x in self.cache:
            return self.cache[x]
        else:
            return None

# 读取容量
input()
capacity = int(input())
cache = NeighborCache(capacity)

while True:
    line = input()
    if line.startswith("write:"):
        # 写入操作
        n = int(input())
        for _ in range(n):
            x, y = map(int, input().split())
            cache.write(x, y)
            cache.timestamp += 1  # 更新时间戳
    elif line.startswith("read:"):
        # 读取操作
        x = int(input())
        cache.read(x)
        cache.timestamp += 1  # 更新时间戳
    elif line.startswith("query:"):
        # 查询输出操作
        x = int(input())
        y = cache.query(x)
        if y is not None:
            print(y)
        else:
            print(-1)
        cache.timestamp += 1  # 更新时间戳
        break


#include <unordered_map>
#include <queue>
#include <tuple>

