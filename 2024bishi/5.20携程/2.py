import heapq

def solve(n, balls):
    dic = {}
    for a, b in balls:
        if a in dic:
            dic[a] += b
        else:
            dic[a] = b
    
    min_heap = []
    for a in dic:
        heapq.heappush(min_heap, a)
    
    while min_heap:
        current = heapq.heappop(min_heap)
        count = dic[current]
        
        pairs = count // 2
        if pairs > 0:
            b = current + 2
            c = pairs
            if b in dic:
                dic[b] += c
            else:
                dic[b] = c
                heapq.heappush(min_heap, b)
        dic[current] = count % 2
    
    result = []
    for a in sorted(dic):
        if dic[a] > 0:
            result.extend([a] * dic[a])
    
    return len(result), result


n = int(input().strip())
balls = []
for _ in range(n):
    a, b = map(int, input().strip().split())
    balls.append((a, b))

m, final_balls = solve(n, balls)

print(m)
print(" ".join(map(str, final_balls)))
