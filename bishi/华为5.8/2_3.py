from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()
        self.usage_count = {}
        self.timestamp = 0

    def write(self, local_cell: int, neighbor_cell: int):
        if local_cell in self.cache:
            # 更新现有的邻区数据
            self.cache.move_to_end(local_cell)
            self.cache[local_cell] = (neighbor_cell, self.timestamp)
            self.usage_count[local_cell] += 1
        else:
            # 添加新的邻区数据
            if len(self.cache) >= self.capacity:
                # 按照使用次数和时间戳找到要删除的项
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
            pass  # 读取不存在的LocalCell，忽略

    def query(self, local_cell: int):
        if local_cell in self.cache:
            return self.cache[local_cell][0]
        else:
            return -1

def process_operations(operations):
    lru_cache = None
    results = []
    write_mode = False
    
    for operation in operations:
        if operation.startswith("capacity:"):
            capacity = int(operation.split(":")[1].strip())
            lru_cache = LRUCache(capacity)
            write_mode = False
        elif operation.startswith("write:"):
            write_mode = True
        elif operation.startswith("read:"):
            local_cell = int(operation.split(":")[1].strip())
            lru_cache.read(local_cell)
            write_mode = False
        elif operation.startswith("query:"):
            local_cell = int(operation.split(":")[1].strip())
            result = lru_cache.query(local_cell)
            results.append(result)
            print(result)
            write_mode = False
        elif write_mode:
            data = operation.strip()
            if data:
                local_cell, neighbor_cell = map(int, data.split())
                lru_cache.write(local_cell, neighbor_cell)
    
    return results

# 测试用例
operations = [
    "capacity: 3",
    "write: 3",
    "1 2",
    "4 3",
    "2 3",
    "read: 2",
    "write: 1",
    "3 1",
    "query: 1"
]

print(process_operations(operations))  # 输出 [-1]
