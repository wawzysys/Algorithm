import heapq
import time

class NeighborCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.usage = []

    def write(self, local_cell, neighbor_cell):
        if local_cell in self.cache:
            # 更新已存在的记录
            self.cache[local_cell] = (neighbor_cell, 0, time.time())
            self.update_usage(local_cell)
        else:
            # 插入新记录
            if len(self.cache) >= self.capacity:
                self.evict()
            self.cache[local_cell] = (neighbor_cell, 0, time.time())
            heapq.heappush(self.usage, (0, time.time(), local_cell))

    def read(self, local_cell):
        if local_cell in self.cache:
            # 更新使用次数和时间
            self.update_usage(local_cell)

    def query(self, local_cell):
        if local_cell in self.cache:
            neighbor_cell, _, _ = self.cache[local_cell]
            return neighbor_cell
        else:
            return -1

    def update_usage(self, local_cell):
        neighbor_cell, usage_count, last_time = self.cache[local_cell]
        usage_count += 1
        last_time = time.time()
        self.cache[local_cell] = (neighbor_cell, usage_count, last_time)
        # 移除原有记录并插入更新后的记录
        self.usage = [(count, last_time, cell) for count, last_time, cell in self.usage if cell != local_cell]
        heapq.heappush(self.usage, (usage_count, last_time, local_cell))

    def evict(self):
        # 选择删除次数最少且最久未使用的记录
        while self.usage:
            _, _, local_cell = heapq.heappop(self.usage)
            if local_cell in self.cache:
                del self.cache[local_cell]
                break

def main():
    _ = input()
    capacity = int(input())
    cache = NeighborCache(capacity)

    while True:
        operation = input()

        if operation == "exit":
            break
        elif operation == "write":
            local_cell, neighbor_cell = map(int, input("请输入 LocalCell 和 NeighborCell: ").split())
            cache.write(local_cell, neighbor_cell)
        elif operation == "read":
            local_cell = int(input("请输入要读取的 LocalCell: "))
            cache.read(local_cell)
        elif operation == "query":
            local_cell = int(input("请输入要查询的 LocalCell: "))
            result = cache.query(local_cell)
            print("查询结果:", result)
        else:
            print("无效的操作，请重新输入。")

if __name__ == "__main__":
    main()
