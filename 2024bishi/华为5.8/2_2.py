cache = {}
usage_count = {}
capacity = 0
timestamp = 0

def write(cell1: int, cell2: int):
    global cache, usage_count, timestamp
    # print(cell1, cell2)
    if cell1 in cache:
        cache[cell1] = (cell2, timestamp)
        usage_count[cell1] += 1
    else:
        if len(cache) >= capacity:
            least_used = min(usage_count.items(), key=lambda x: (x[1], cache[x[0]][1]))
            del cache[least_used[0]]
            del usage_count[least_used[0]]
        cache[cell1] = (cell2, timestamp)
        usage_count[cell1] = 1
    timestamp += 1

def read(cell: int):
    global cache, usage_count, timestamp
    if cell in cache:
        cache[cell] = (cache[cell][0], timestamp)
        usage_count[cell] += 1
        timestamp += 1

def query(cell: int):
    global cache
    if cell in cache:
        return cache[cell][0]
    else:
        return -1

def solve():
    global cache, capacity, usage_count, timestamp
    while True:
        try:
            x = input()
            # print(x)
            if x == "capacity:":
                capacity = int(input())
            elif x == "write:":
                cnt = int(input())
                for _ in range(cnt):
                    cell1, cell2 = map(int, input().split())
                    # print(cell1, cell2)
                    write(cell1, cell2)
                    # print(cache)
            elif x == "read:":
                cell = int(input())
                read(cell)
            elif x == "query:":
                cell = int(input())
                result = query(cell)
                print(result)
        except:
            break

solve()


