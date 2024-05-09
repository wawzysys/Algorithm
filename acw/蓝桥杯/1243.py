#/E/0Code/Algorithm/acw/蓝桥杯/1243.py
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
# write=lambda x:sys.stdout.write(str(x)+'\n')
# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
from collections import *
# from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
from math import *
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))
def solve():
    n, m, k = mint()
    can = [lint() for _ in range(n)]
    vis = set()  # 使用集合而不是列表
    ans = inf
    N = [0] * (n + 1)
    def dfs(u, t, ans, vis):
        if len(vis) == m:  # 直接检查vis的大小
            ans = min(ans, u)
            return ans
        if u >= ans:
            return ans
        for i in range(t, n):
            if N[i] == 0:
                vis_backup = vis.copy()  # 备份当前vis状态
                for c in can[i]:
                    vis.add(c)  # 添加元素到集合
                N[i] = 1
                ans = dfs(u + 1, i + 1, ans, vis)
                vis = vis_backup  # 恢复vis状态
                N[i] = 0
        return ans
    ans = dfs(0, 0, ans, vis)
    print(-1 if ans == inf else ans)






if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()