import heapq
def solve(n, times):
    min_heap = []
    cur = 0
    tol = 0
    for ti, wi in times:
        if cur < ti:
            cur = ti
        heapq.heappush(min_heap, (wi, ti))
        while min_heap and cur >= min_heap[0][1]:
            a, b = heapq.heappop(min_heap)
            cur += a
            tol += (cur - b)
    while min_heap:
        a, b = heapq.heappop(min_heap)
        cur += a
        tol += (cur - b)
    return tol
n = int(input())
times = []
for _ in range(n):
    a, b = map(int, input().split())
    times.append((a, b))
result = solve(n, times)
print(result)
