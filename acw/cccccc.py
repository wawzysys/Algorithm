import sys
import heapq
from heapq import heapify, heappop, heappush, heapreplace, heappushpop


input = lambda: sys.stdin.readline().rstrip()
sint = lambda: int(input())
mint = lambda: map(int, input().split())
ints = lambda: list(map(int, input().split()))

def solve() -> None:
    n, k = mint()
    a = [ints() for i in range(n)]
    
    step_queues = [[] for _ in range(k)]
    
    ans = 0

    for _ in range(n):
        cur = 0  # 每个蛋糕开始的时间
        for step in range(k):
            t = a[step][1]
            if len(step_queues[step]) < a[step][0]:
                # 如果当前步骤队列未满，直接添加任务
                heapq.heappush(step_queues[step], cur + t)
            else:
                # 如果当前步骤队列已满，替换最早完成的任务
                # 更新cur为当前步骤可开始的最早时间
                cur = heapq.heappushpop(step_queues[step], cur + t)
            cur += t
            ans = max(ans, cur)
    print(ans)


if __name__ == '__main__':
    solve()