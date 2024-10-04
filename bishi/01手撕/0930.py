
from collections import *
def f(arr, val):
    index_map = defaultdict(int)
    n = len(arr)
    for i in range(n):
        co = val - arr[i]
        if co in index_map:
            return [index_map[co], i]
        index_map[arr[i]] = i

创建一个哈希表：用于存储数组中的元素及其索引。
遍历数组：对于每个元素，计算其所需的配对值（即 val - arr[i]）。
检查哈希表：如果配对值存在于哈希表中，返回当前索引和配对值的索引。
更新哈希表：如果配对值不存在，则将当前元素及其索引存入哈希表。