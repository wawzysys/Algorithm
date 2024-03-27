#/E/0Code/Algorithm/acw/acw4656.py
import sys
sys.setrecursionlimit(100000)
input=lambda:sys.stdin.readline().strip()
# write=lambda x:sys.stdout.write(str(x)+'\n')
# from decimal import Decimal
# from datetime import datetime,timedelta
# from random import randint
# from copy import deepcopy
from collections import *
from heapq import heapify,heappush,heappop
# from bisect import bisect_left,bisect,insort
from math import *
# from functools import cmp_to_key,reduce
# from operator import or_,xor,add,mul
# from itertools import permutations,combinations,accumulate
sint = lambda: int(input())
mint = lambda: map(int, input().split())
lint = lambda: list(map(int, input().split()))

# def solve():
# 	n, m = mint()
# 	ans = []
# 	for i in range(n):
# 		a, b = mint()
# 		while a > 0:
# 			ans.append(a)
# 			a -= b
# 	ans.sort(reverse = True)
# 	ss = sum(ans[0 : min(m, len(ans))])
# 	print(ss)



def solve():
    n, m = mint()  # 假设 mint() 是一个输入函数
    heap = []  # 创建一个空堆

    for _ in range(n):
        a, b = mint()
        while a > 0:
            if len(heap) < m:
                heappush(heap, a)
            elif a > heap[0]:  # 仅当当前值大于堆顶元素时才操作
                heappush(heap, a)  # 先推入新元素
                heappop(heap)  # 然后弹出最小元素
            a -= b  # 减去b继续循环

    # 计算堆中所有元素的和
    ss = sum(heap)
    print(ss)


if __name__ == '__main__':
	#t=int(input())
	#for _ in range(t):
	#   solve()

	solve()
